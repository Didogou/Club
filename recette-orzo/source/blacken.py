import numpy as np,sys
from PIL import Image,ImageFilter
def ramp(x,a,b): return np.clip((x-a)/(b-a),0,1)
def fix(im):
    a=np.asarray(im.convert('RGB')).astype(np.float32)/255
    R,G,B=a[...,0],a[...,1],a[...,2]
    v=a.max(2);sat=(v-a.min(2))/np.maximum(v,1e-3)
    # traces d'éponge : gris clair froid (bleuté), sur fond noir ; on épargne cheveux, veste, poêle (tons chauds)
    w=ramp(v,.19,.27)*(1-ramp(v,.80,.92))*ramp(B-R,-.015,.03)*(1-ramp(sat,.28,.36))
    w=np.asarray(Image.fromarray((w*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(2))).astype(np.float32)/255
    target=0.15+(v-0.15).clip(0)*0.12
    newv=v*(1-w)+np.minimum(v,target)*w
    out=(a*(newv/np.maximum(v,1e-3))[...,None]).clip(0,1)
    return Image.fromarray((out*255+.5).astype(np.uint8))
if __name__=='__main__':
    for f in sys.argv[1:]: fix(Image.open(f)).save(f.replace('.png','_n.png'))
