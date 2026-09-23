# Pub TikTok — Karine Diététique

- `karine-dietetique-tiktok.mp4` : vidéo finale (35 s, 1080×1920, 30 fps).
- `source/index.html` : l'animation (fonction `seek(t)` qui dessine l'image à l'instant t).
- `source/render.js` : capture les images avec Playwright.

Régénérer :

```bash
cd pub-tiktok/source
npm i playwright-core
node render.js full   # images dans frames/
ffmpeg -framerate 30 -i frames/%05d.jpg -c:v libx264 -crf 18 -pix_fmt yuv420p ../karine-dietetique-tiktok.mp4
```

Les images de `source/a/` viennent de `CLAUDE-PROJETS/karine-social-media/public`.
