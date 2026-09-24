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
