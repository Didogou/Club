# Les Tutos de Karine

## #1 · De la recette à ton assiette
`tuto-01-de-la-recette-a-ton-assiette.mp4` — 34 s, 1080×1920, muette (musique à ajouter sur TikTok/Instagram).

Parcours : accueil → recettes → fiche cordon-bleu → « + Mes courses » (4 personnes) → liste de courses cochée
→ mode pas à pas → « Fait » → « Ajouter à mon dîner » → Mes repas.

## Faire un nouveau tuto
Tout se règle dans la liste `S` de `source/index.html` : une ligne par écran
(image, durée, chapitre, taps et zoom en coordonnées de la capture d'origine 1080 × 2640).
Les chapitres sont dans `CH`. Captures : Drive « Karine Tuto », status bar rognée (106 px).
Rendu : `node render.js full` puis ffmpeg (voir `pub-tiktok/README.md`).

## #1 (version vidéo sous-titrée) · De la recette à ton assiette
`tuto-01-video-de-la-recette-a-ton-assiette.mp4` — 2 min 46, 5 étapes avec écran titre, texte en bulle posée sur l’image figée, à partir de l'enregistrement d'écran `source-video/tuto2.mp4`
(Tortillas au poulet et crudités). Pauses sur chaque action, sous-titres « Karine », cercle « ici » sur chaque bouton.

Refaire / modifier :
```bash
cd tutos-karine/source-video
mkdir -p a/v && ffmpeg -i tuto2.mp4 -t 85 -q:v 3 a/v/%05d.jpg   # images de la vidéo source
npm i playwright-core && node render.js full
```
Tout le découpage est dans la liste `G` de `index.html` : une ligne par moment (pause `hold` ou lecture `play`),
avec le sous-titre, le tap (x, y en pixels de la vidéo 540 × 1288) et le zoom.

## #2 · Compose ton menu
`tuto-02-compose-ton-menu.mp4` — 2 min 08 (version rythmée : bulles plus courtes, lectures ×2), même style que le #1 vidéo, à partir de l'enregistrement d'écran
`source-menu/compose-menu-light.mp4` (3 min 28, 540 × 1080 affiché en 540 × 1288).

5 étapes : ouvrir « Compose ton menu » → choisir les plats du lundi (vitesse normale, bulles : onglets, recherche,
filtres, collections, nombre de personnes, fiche recette) → remplir le reste de la semaine **en accéléré ×8**
(pastille « ⏩ accéléré », une astuce figée : glisser-déposer d'un plat)
→ écran récap **« Ta semaine est prête ! »** (toute la semaine, déjeuner/dîner) → « Ajouter au panier »
→ Mes courses (menu de la semaine, rayons, cases à cocher).

Refaire / modifier :
```bash
cd tutos-karine/source-menu
mkdir -p a/v && ffmpeg -i compose-menu-light.mp4 -vf "fps=30,scale=540:1288,setsar=1" -q:v 3 a/v/%05d.jpg
npm i playwright-core && node render.js full
ffmpeg -framerate 30 -i frames/%05d.jpg -f lavfi -i anullsrc=r=44100:cl=stereo -shortest \
  -c:v libx264 -crf 23 -pix_fmt yuv420p -c:a aac ../tuto-02-compose-ton-menu.mp4
```
Le découpage est dans la liste `G` de `index.html` (comme le #1 ; `v` = vitesse de lecture, `recap` = écran semaine).
Le récap est dans `WEEK`, avec les vignettes recadrées dans la vidéo source (`a/w/`).
Illustrations des écrans titres (`a/c1…c4`) : `karine-social-media/public` du dépôt CLAUDE-PROJETS.
