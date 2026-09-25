"""Assemble les 4 étapes en une version complète (≤ 3 min) et un best-of court."""
import subprocess, imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
D = '/home/user/Club/recette-orzo/'
F = {0: D+'couverture.mp4', 5: D+'carte-appli.mp4', 1: D+'etape-1-ingredients.mp4', 2: D+'etape-2-sauteuse.mp4',
     3: D+'etape-3-saumon-butternut.mp4', 4: D+'etape-4-creme-citron-aneth.mp4'}

def build(segs, out):
    """segs : liste de (étape, début, fin, facteur d'accélération)."""
    inputs = sorted({s[0] for s in segs})
    idx = {n: i for i, n in enumerate(inputs)}
    args = [FF, '-y', '-loglevel', 'error']
    for n in inputs: args += ['-i', F[n]]
    fc = []
    for k, (n, a, b, sp) in enumerate(segs):
        fc.append(f"[{idx[n]}:v]trim={a}:{b},setpts=(PTS-STARTPTS)/{sp},fps=30[s{k}]")
    fc.append(''.join(f'[s{k}]' for k in range(len(segs))) + f"concat=n={len(segs)}:v=1:a=0[v]")
    args += ['-f', 'lavfi', '-i', 'anullsrc=r=44100:cl=stereo', '-filter_complex', ';'.join(fc),
             '-map', '[v]', '-map', f'{len(inputs)}:a', '-shortest',
             '-c:v', 'libx264', '-preset', 'slow', '-crf', '24', '-pix_fmt', 'yuv420p',
             '-movflags', '+faststart', '-c:a', 'aac', '-b:a', '64k', out]
    subprocess.run(args, check=True)

OUT = 3.4  # durée de l'écran de fin de chaque étape
# Version complète : écrans de fin intermédiaires retirés, passages accélérés encore un peu plus rapides pour tenir en 3 min
full = [
    # Couverture puis directement la recette (écran titre étape 1 + ingrédients)
    (0, 0, 1.6, 1), (1, 22.6, 43.35 - OUT, 1.15),
    # Étape 2
    (2, 0, 2.8, 2.5), (2, 2.8, 11.3, 1.3), (2, 11.3, 22.1, 2.5), (2, 22.1, 27.9, 1.3),
    (2, 27.9, 40.8, 2.8), (2, 40.8, 46.41 - OUT, 1),
    # Étape 3
    (3, 0, 2.8, 2.5), (3, 2.8, 18.3, 2.5), (3, 18.3, 24.1, 1.5), (3, 24.1, 34.0, 1.6), (3, 34.0, 42.25 - OUT, 1),
    # Étape 4 jusqu'à l'assiette
    (4, 0, 2.8, 2.5), (4, 2.8, 12.3, 1.8), (4, 12.3, 17.3, 1.6), (4, 17.3, 22.3, 1), (4, 22.3, 27.3, 1.6),
    (4, 27.3, 42.9, 1.4), (4, 42.9, 54.1, 3), (4, 54.1, 63.1, 1.8), (4, 63.1, 74.35 - OUT, 1),
    # À la fin : retrouve les recettes de Karine dans l'appli (recherche de la recette), puis écran de fin
    (5, 0, 2.2, 1), (1, 2.8, 6.0, 1.6), (1, 6.0, 9.9, 1), (1, 9.9, 14.1, 1.6), (1, 14.1, 16.4, 1), (1, 16.4, 19.8, 1.6),
    (4, 74.35 - OUT, 74.35, 1),
]
# Best-of ~28 s, rythme nerveux
short = [
    (0, 0, 1.6, 1),         # couverture : Recette en vidéo + assiette
    (1, 23.0, 31.0, 3),     # les ingrédients étiquetés
    (2, 2.8, 8.3, 2),       # l'orzo dans le bouillon
    (2, 11.3, 22.1, 4),     # l'oignon
    (3, 3.0, 13.0, 4),      # le saumon en cubes
    (3, 24.1, 31.0, 2.2),   # butternut + saumon dans la sauteuse
    (4, 17.3, 21.3, 1.2),   # l'opercule 😂
    (4, 33.3, 38.9, 2),     # le citron
    (4, 63.1, 66.8, 1.3),   # la dernière étape cochée
    (4, 74.35 - OUT, 74.35, 1.2),  # écran de fin
]
build(full, D + 'one-pot-orzo-complet.mp4')
# build(short, D + 'one-pot-orzo-best-of.mp4')  # best-of inchangé
