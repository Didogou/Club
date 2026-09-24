# Passation — Vidéos Karine Diététique

Tout le travail est sur la branche **`claude/tiktok-ad-creation-a8nfbb`** du dépôt `Didogou/Club`.
Interlocuteur : Didier (gère l'appli de Karine Piffaretti, diététicienne-nutritionniste, karine-dietetique.fr,
Instagram @karine_dieteticienne). On parle en français, on tutoie dans les vidéos (« tu »).

## ✅ Fait : Tuto « Compose ton menu » (`tutos-karine/tuto-02-compose-ton-menu.mp4`, 4 min 19)
Source et découpage dans `tutos-karine/source-menu/` (voir `tutos-karine/README.md`). La vidéo a été déposée
directement sur la branche (le connecteur Drive échouait sur ce fichier de 7,9 Mo). En attente des retours de Didier.

### Demande d'origine
- Vidéo source sur Google Drive : **`compose-menu-light.mp4`** (7,9 Mo, id `1QjjGy2xO2gOgWyPYkfbQT5Ar2Ka-mY11`,
  dossier id `1hnLX1XBP61fBCng6DZE6J2kiAT33ZZjz`). Enregistrement d'écran de 3 min 27.
- Demande explicite : **accélérer la phase de remplissage des jours** (garder le 1er jour à vitesse normale avec
  bulle explicative, puis accéléré ×3-4, puis pause sur la semaine complète).
- Faire exactement le même style que le tuto #1 vidéo (`tutos-karine/source-video/index.html`) :
  écran d'intro « Les Tutos de Karine » → écran « Je vais te guider pour … » → pour chaque étape un **écran titre
  plein écran** (« Étape n / N » + titre + illustration de l'appli) → scène.

## ✅ Règles de style validées par Didier (très important)
1. Le public n'est **pas technophile** : c'est lent, avec des pauses.
2. **Le texte est dans une bulle posée sur l'image**, avec une flèche vers le bouton concerné, et l'avatar de Karine.
   **L'image est figée pendant la lecture** (pastille « ⏸ pause »). Durée de lecture ≈ 0,8 + max(2,6 ; nb_caractères/14) + 0,6 s.
3. **Pas de texte pendant les passages où l'écran défile** : on lit d'abord (image figée), puis on regarde.
4. Cercle rose pulsant sur chaque bouton à toucher + zoom centré sur la zone (sans montrer les bords de la capture).
5. Écran titre plein écran avant chaque étape. Titres formulés comme Didier les a donnés, par exemple :
   « Utilise l'application quand tu fais tes courses », « Lorsque tu cuisines, utilise l'application »,
   « Ajoute la recette à tes repas ».
6. Couper les écrans de chargement, masquer toute trace d'administration (ex. ligne « ANCRAGE (ADMIN) »).
7. Fin : « Retrouve tous les tutos dans l'appli », Karine DIÉTÉTIQUE, karine-dietetique.fr, @karine_dieteticienne.
8. Charte : rose `#e0527a`, bordeaux `#7a1f3d`, crème `#fff6f4`, polices Nunito / Dancing Script / Allura,
   fond fleuri de l'appli, avatar illustré de Karine.

## 🛠️ Méthode technique
- Outils : `pip install pillow imageio-ffmpeg` (ffmpeg via `imageio_ffmpeg.get_ffmpeg_exe()`),
  `npm i playwright-core`, Chromium : `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`.
- Rendu : page HTML 1080×1920 avec une fonction `window.seek(t)` ; `render.js` capture chaque image (30 i/s),
  puis ffmpeg : `-framerate 30 -i frames/%05d.jpg -f lavfi -i anullsrc … -c:v libx264 -crf 20-25 -pix_fmt yuv420p`.
  Pour les tutos à partir d'une vidéo : extraire les images de la source (`ffmpeg -i src.mp4 a/v/%05d.jpg`),
  la page affiche l'image correspondant à l'instant source, et `render.js` attend `window.ready()`.
- Repérage : planches 1 image/seconde (`fps=1,scale=180:-1,tile=10x2`) puis images clés avec règles de coordonnées.
- **Google Drive** : le connecteur ne télécharge que les fichiers **< 10 Mo** ; la réponse (base64) est enregistrée dans
  un fichier `tool-results/…txt` → le décoder en Python (`json.load` puis `base64.b64decode(d['content'])`).
  Si la vidéo est trop lourde : HandBrake, préréglage **General → Very Fast 1080p30**, onglet Vidéo **débit moyen 300**,
  sans audio. Ne jamais utiliser un préréglage « 360p » (écrase la vidéo verticale).
- Envoi au user : `SendUserFile` limité à 30 Mo (baisser le CRF si besoin).
- Le code de l'appli (captures, icônes, polices, fiches recettes) est dans le dépôt `Didogou/CLAUDE-PROJETS`,
  dossier `karine-social-media/public` (à ajouter avec `add_repo` puis cloner).

## 📁 Ce qui existe déjà
| Dossier | Contenu |
|---|---|
| `pub-tiktok/` | Pub TikTok de l'appli (48 s) + source. |
| `video-recettes/` | « 4 recettes pour gâter maman » (fiches + étapes de préparation). |
| `tutos-karine/` | Tuto #2 « Compose ton menu » (`tuto-02-…mp4`, source `source-menu/`). Tuto #1 en captures (`tuto-01-…assiette.mp4`) et **tuto #1 vidéo sous-titrée** (`tuto-01-video-…mp4`, 2 min 46, le modèle à suivre) + sources. |

## ❓ Questions encore ouvertes (pub TikTok)
- Fin de la pub : « Enfin tu vois… » → actuellement « tes progrès » (à confirmer).
- Prix affiché : « dès 5 € par mois » (5 € = formule patient·e, 8 € = grand public) → à confirmer.

## 🗓️ Plus tard
- Reel « mains de Karine » : Karine filme en vue de dessus (cheesecake fraise-citron, plan de tournage fourni),
  dépose les clips dans Drive, montage accéléré + texte des étapes.
- Autres tutos proposés : scanner son assiette, livre de recettes, suivi du poids.
