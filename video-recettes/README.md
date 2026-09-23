# Vidéo « 4 recettes pour gâter maman »

- `gateau-pour-maman.mp4` : vidéo finale (45 s, 1080×1920, 30 fps, muette — ajouter la musique sur TikTok/Instagram).
- `source/index.html` : l'animation. La liste `R` en haut du script décrit les 4 recettes
  (fiche, nombre d'étapes, nom, kcal) : c'est le seul endroit à modifier pour faire la même vidéo avec d'autres fiches.
- `source/crops.py` : découpe les étapes de préparation dans les fiches (coordonnées par fiche).
- Rendu : voir `pub-tiktok/README.md` (même méthode : `node render.js full` puis ffmpeg).

Les fiches viennent de `CLAUDE-PROJETS/karine-social-media/public/images/recipes/gateau-maman`.
