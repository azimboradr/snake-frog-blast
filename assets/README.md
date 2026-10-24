# Snake Frog Rush — Asset pipeline (Test 9 preparation)

This folder is for **real, separately licensed 3D assets**, not procedurally combined spheres.

## Asset acceptance checklist
- GLB/glTF 2.0 with real geometry, UVs and PBR materials
- source URL, author, license, attribution and download date recorded
- verified original download (not a preview image or hotlinked demo)
- inspect appearance from the game's actual overhead camera
- test loading, animation, iPhone Safari frame rate and memory
- fall back safely to existing Test 8 visuals if an asset cannot load
- avoid extra requests and uncontrolled CDN hotlinks in final production

## Candidate source (not yet integrated)
- Frog, Quaternius, Poly Pizza: https://poly.pizza/m/37wofOCOzG
- Reported CC0 and animated; verify license in original download.
- Other candidate CC0 asset libraries: https://polyhaven.com/ , https://quaternius.com/

## Status
Test 8 is a procedural prototype, NOT the target-quality scene.
No third-party 3D asset has been downloaded or integrated yet.
Do not announce a graphical breakthrough before visual and mobile verification.

## Integration order
1. Frog GLB: verify source, import, orient, scale, animate, replace procedural frog.
2. Trees and forest rocks/logs: replace primitive silhouettes with textured meshes.
3. Spider GLB: articulated animation; retain collision geometry.
4. Snake: bespoke skinned continuous mesh with proper UVs and PBR scale/normal maps.
5. Forest terrain: tiled PBR materials, organic blends, vegetation instancing, water.
6. Mobile QA: verify controls unchanged, no stalls, texture and geometry budgets.

## Non-regression
Preserve Test 6/7 steering exactly, old versions, open playfield, HUD and collision logic.
