set -e
cd /tmp/claude-0/-home-user-Club/816ddba1-4aa8-5d5b-a66f-e066d5963682/scratchpad/parm
FF=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
R=/home/user/Club/recette-orzo; D=/home/user/Club/recette-parmentier
node renderP.js parm.html 0 frames full
$FF -y -loglevel error -framerate 30 -i frames/%05d.jpg -i $R/carte-appli.mp4 -i $R/etape-4-creme-citron-aneth.mp4 -f lavfi -i anullsrc=r=44100:cl=stereo -filter_complex "[0:v]fps=30,setpts=PTS-STARTPTS[a];[1:v]fps=30,setpts=PTS-STARTPTS[b];[2:v]trim=70.95:74.35,setpts=PTS-STARTPTS,fps=30[c];[a][b][c]concat=n=3:v=1:a=0[v]" -map "[v]" -map 3:a -shortest -c:v libx264 -preset slow -crf 22 -pix_fmt yuv420p -movflags +faststart -c:a aac -b:a 64k $D/parmentier-tiktok.mp4
$FF -y -loglevel error -i $D/parmentier-tiktok.mp4 -c:v libx264 -crf 28 -preset fast -c:a copy ../parmentier-tiktok-envoi.mp4
cp parm.html renderP.js build.sh $D/source/
$FF -y -loglevel error -ss 51 -i $D/parmentier-tiktok.mp4 -frames:v 1 -vf scale=400:-1 chkf.png
