import os, math, numpy as np, trimesh
from PIL import Image, ImageDraw
os.makedirs('assets/models',exist_ok=True)
def matmesh(mesh,color):
 mesh.visual=trimesh.visual.TextureVisuals(uv=np.zeros((len(mesh.vertices),2)),material=trimesh.visual.material.PBRMaterial(baseColorFactor=color,metallicFactor=0,roughnessFactor=.85))
 return mesh
def ellipsoid(center,scale,color,sub=2):
 m=trimesh.creation.icosphere(subdivisions=sub,radius=1);m.apply_scale(scale);m.apply_translation(center);return matmesh(m,color)
def tube(a,b,r,color):
 a=np.array(a);b=np.array(b);d=b-a
 m=trimesh.creation.cylinder(radius=r,height=np.linalg.norm(d),sections=9)
 m.apply_transform(trimesh.geometry.align_vectors([0,0,1],d))
 m.apply_translation((a+b)/2)
 return matmesh(m,color)
green=[69,154,50,255];dark=[30,95,36,255];gold=[215,183,91,255];black=[17,30,18,255];pale=[185,204,113,255]
parts=[ellipsoid([0,.36,.18],[.42,.27,.53],green,3),ellipsoid([0,.4,-.36],[.49,.24,.37],green,3),ellipsoid([0,.22,-.4],[.35,.09,.28],pale)]
for s in (-1,1):
 parts.extend([ellipsoid([s*.33,.6,-.48],[.17,.19,.18],green),ellipsoid([s*.34,.65,-.59],[.115,.12,.08],gold),ellipsoid([s*.34,.66,-.66],[.053,.07,.026],black),ellipsoid([s*.43,.24,.43],[.25,.24,.29],green)])
 for a,b,r in [([s*.44,.25,.43],[s*.64,.11,.67],.095),([s*.64,.11,.67],[s*.47,.05,.8],.055),([s*.31,.27,-.24],[s*.46,.09,-.48],.055)]:
  parts.append(tube(a,b,r,green))
 for t in (-1,0,1):
  parts.append(tube([s*.47,.05,.79],[s*(.47+t*.09),.04,.97],.024,green))
  parts.append(tube([s*.46,.06,-.48],[s*(.46+t*.065),.04,-.63],.019,green))
frog=trimesh.Scene()
for i,p in enumerate(parts):frog.add_geometry(p,node_name='frog_part_'+str(i))
frog.export('assets/models/frog_detailed.glb')
# UV-mapped snake mesh with authored color/normal/roughness images
W=512;H=512
img=Image.new('RGB',(W,H),(73,133,56));d=ImageDraw.Draw(img)
for row in range(42):
 for col in range(32):
  x=col*16+(row%2)*8;y=row*13
  c=(54+(row+col)%4*7,113+(row*3+col)%5*8,43+(col%3)*6)
  d.ellipse((x-7,y-5,x+7,y+7),fill=c,outline=(106,161,77),width=1)
img.save('assets/models/snake_albedo.png')
normal=Image.new('RGB',(W,H),(128,128,255));normal.save('assets/models/snake_normal.png')
rough=Image.new('RGB',(W,H),(204,204,204));rough.save('assets/models/snake_roughness.png')
verts=[];uv=[];faces=[];rings=80;sides=20
for i in range(rings+1):
 z=-5.8*i/rings;r=.34*(min(1,(rings-i)/9)*.95+.05)
 for j in range(sides+1):
  a=j/sides*2*math.pi
  verts.append([math.cos(a)*r,.36+math.sin(a)*r*.82,z])
  uv.append([j/sides,i/rings*3])
for i in range(rings):
 for j in range(sides):
  a=i*(sides+1)+j;b=a+sides+1;faces.extend([[a,b,a+1],[b,b+1,a+1]])
body=trimesh.Trimesh(vertices=verts,faces=faces,process=False)
texture=trimesh.visual.material.PBRMaterial(baseColorTexture=img,normalTexture=normal,metallicRoughnessTexture=rough,roughnessFactor=.8,metallicFactor=0)
body.visual=trimesh.visual.TextureVisuals(uv=np.array(uv),material=texture)
snake=trimesh.Scene();snake.add_geometry(body,node_name='snake_body')
for i,p in enumerate([ellipsoid([0,.37,.20],[.44,.27,.52],green,3),ellipsoid([0,.29,-.24],[.37,.16,.32],green,3),ellipsoid([0,.22,-.34],[.34,.09,.25],pale)]):
 snake.add_geometry(p,node_name='snake_head_'+str(i))
for s in (-1,1):
 snake.add_geometry(ellipsoid([s*.30,.53,-.12],[.13,.14,.13],gold),node_name='eye_'+str(s))
 snake.add_geometry(ellipsoid([s*.32,.54,-.22],[.058,.075,.04],black),node_name='pupil_'+str(s))
snake.export('assets/models/snake_uv_pbr.glb')
print('Generated frog and UV/PBR snake GLBs')
