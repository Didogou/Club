set -e
cd /tmp/claude-0/-home-user-Club/816ddba1-4aa8-5d5b-a66f-e066d5963682/scratchpad/recette
FF=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
for s in "v201926484 v2 320" "v202031886 v3 320" "v204830495 v4 120" "etape3 k3 120"; do set -- $s; rm -rf a/$2; mkdir -p a/$2; $FF -loglevel error -y -i $1.mp4 -vf "crop=960:720:$3:0,scale=1080:810" -q:v 3 a/$2/%04d.jpg; done
python3 blk_dir.py a/v2 a/v3 a/v4 a/k3
for n in 2 3 4; do node render$n.js full >/dev/null; done
node renderC.js full >/dev/null
$FF -y -loglevel error -framerate 30 -i framesC/%05d.jpg -c:v libx264 -crf 20 -pix_fmt yuv420p /home/user/Club/recette-orzo/couverture.mp4
cp previewC/t0.jpg /home/user/Club/recette-orzo/couverture-insta.jpg
for p in "2 etape-2-sauteuse" "3 etape-3-saumon-butternut" "4 etape-4-creme-citron-aneth"; do set -- $p; $FF -y -loglevel error -framerate 30 -i frames$1/%05d.jpg -f lavfi -i anullsrc=r=44100:cl=stereo -shortest -c:v libx264 -preset slow -crf 23 -pix_fmt yuv420p -movflags +faststart -c:a aac -b:a 64k /home/user/Club/recette-orzo/$2.mp4; done
python3 assemble.py
$FF -y -loglevel error -i /home/user/Club/recette-orzo/one-pot-orzo-complet.mp4 -c:v libx264 -preset slow -crf 28 -pix_fmt yuv420p -movflags +faststart -c:a copy ../one-pot-orzo-complet-envoi.mp4
for f in /home/user/Club/recette-orzo/one-pot*.mp4 ../one-pot-orzo-complet-envoi.mp4; do echo "$f $($FF -i $f 2>&1 | grep -o 'Duration: [0-9:.]*') $(stat -c %s $f)"; done
echo FIN
