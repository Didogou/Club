set -e
cd /tmp/claude-0/-home-user-Club/816ddba1-4aa8-5d5b-a66f-e066d5963682/scratchpad/recette
FF=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
mkdir -p /home/user/Club/recette-orzo/tiktok
node renderTT.js etape2.html 180 framesT2 full & node renderTT.js etape3.html 180 framesT3 full & node renderTT.js etape4.html 180 framesT4 full & wait
for n in 2 3 4; do $FF -y -loglevel error -framerate 30 -i framesT$n/%05d.jpg -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p /home/user/Club/recette-orzo/tiktok/tiktok-etape-$n.mp4 & done; wait
python3 assemble.py tiktok
$FF -y -loglevel error -i /home/user/Club/recette-orzo/one-pot-orzo-tiktok.mp4 -c:v libx264 -preset slow -crf 28 -pix_fmt yuv420p -movflags +faststart -c:a copy ../one-pot-orzo-tiktok-envoi.mp4
$FF -i /home/user/Club/recette-orzo/one-pot-orzo-tiktok.mp4 2>&1 | grep Duration; ls -la ../one-pot-orzo-tiktok-envoi.mp4
echo FIN
