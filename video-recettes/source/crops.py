from PIL import Image
P='/home/user/claude-projets/karine-social-media/public/images/recipes/gateau-maman/'
F={1:(805,1072,[88,290,497,707,915]),2:(760,1030,[100,300,500,700,905,1110]),4:(765,1045,[125,320,512,712,905,1105]),5:(770,1040,[113,305,502,695,892,1103])}
W=200
sheet=Image.new('RGB',(W*6,300*4),'white')
for r,(k,(y0,y1,cs)) in enumerate(F.items()):
  im=Image.open(P+f'{k}.png').convert('RGB')
  for i,c in enumerate(cs):
    x0=max(0,c-W//2);cr=im.crop((x0,y0,x0+W,y1));cr.save(f'a/s{k}-{i+1}.png');sheet.paste(cr,(i*W,r*300))
sheet.save('stepsheet.png')
