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
