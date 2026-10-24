/* Snake Frog Rush — Test 9 procedural PBR texture pack.
   Maps: baseColor (sRGB), normal (linear), roughness (linear).
   Deterministic generated CanvasTextures; no external image dependency. */
(function(global){
'use strict';
function build(THREE,renderer){
 const specs={grass:{base:[99,137,72],rough:.93,grain:6,seed:71},snake:{base:[80,149,59],rough:.57,grain:13,seed:97},forest:{base:[107,84,60],rough:.89,grain:19,seed:131},rock:{base:[125,136,122],rough:.94,grain:9,seed:193}};
 function make(kind){
  const cfg=specs[kind],n=256,canvas=document.createElement('canvas'),rough=document.createElement('canvas'),normal=document.createElement('canvas');
  canvas.width=canvas.height=rough.width=rough.height=normal.width=normal.height=n;
  const ctx=canvas.getContext('2d'),rctx=rough.getContext('2d'),nctx=normal.getContext('2d');
  const a=ctx.createImageData(n,n),b=rctx.createImageData(n,n),c=nctx.createImageData(n,n),heights=new Float32Array(n*n);
  let seed=cfg.seed;const rnd=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed/4294967296};
  for(let y=0;y<n;y++)for(let x=0;x<n;x++){
   const k=y*n+x,u=x/n,v=y/n;
   const scale=kind==='snake'?(Math.cos((u+(Math.floor(v*38)%2)*.013)*Math.PI*38)*Math.cos(v*Math.PI*76)):kind==='forest'?Math.sin(u*150+Math.sin(v*12)*3):Math.sin(u*69)*Math.cos(v*73);
   const noise=(rnd()-.5)*.5,pattern=scale*.3+noise;
   heights[k]=pattern;
   const shade=pattern*cfg.grain+(rnd()-.5)*cfg.grain;
   for(let ch=0;ch<3;ch++)a.data[k*4+ch]=Math.max(0,Math.min(255,cfg.base[ch]+shade));
   a.data[k*4+3]=255;
   const rv=Math.round(Math.max(0,Math.min(255,(cfg.rough+pattern*.075)*255)));
   b.data[k*4]=b.data[k*4+1]=b.data[k*4+2]=rv;b.data[k*4+3]=255;
  }
  for(let y=0;y<n;y++)for(let x=0;x<n;x++){
   const k=y*n+x,l=heights[y*n+(x+n-1)%n],r=heights[y*n+(x+1)%n],up=heights[((y+n-1)%n)*n+x],down=heights[((y+1)%n)*n+x];
   const dx=(r-l)*.65,dy=(down-up)*.65,len=Math.hypot(dx,dy,1);
   c.data[k*4]=Math.round(255*(1-dx/len)/2);c.data[k*4+1]=Math.round(255*(1-dy/len)/2);c.data[k*4+2]=Math.round(255*(1+1/len)/2);c.data[k*4+3]=255;
  }
  ctx.putImageData(a,0,0);rctx.putImageData(b,0,0);nctx.putImageData(c,0,0);
  function tex(cv,srgb){const t=new THREE.CanvasTexture(cv);t.wrapS=t.wrapT=THREE.RepeatWrapping;t.colorSpace=srgb?THREE.SRGBColorSpace:THREE.NoColorSpace;t.anisotropy=Math.min(4,renderer.capabilities.getMaxAnisotropy());return t}
  return {map:tex(canvas,true),normalMap:tex(normal,false),roughnessMap:tex(rough,false)};
 }
 const cache={};return {get(kind){return cache[kind]||(cache[kind]=make(kind))},dispose(){for(const p of Object.values(cache))for(const t of Object.values(p))t.dispose()}};
}
global.SnakeFrogPBR={build};
})(window);
