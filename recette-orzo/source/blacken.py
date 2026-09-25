import numpy as np,sys,cv2
from PIL import Image,ImageFilter
def ramp(x,a,b): return np.clip((x-a)/(b-a),0,1)
K=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(17,17))
def reflets(v,sat):
    """Masque des reflets de lampes : taches claires peu colorées, assez grandes, entourées du noir de la plaque."""
    br=((v>.50)&(sat<.30)).astype(np.uint8)
    br=cv2.morphologyEx(br,cv2.MORPH_OPEN,K)            # retire les objets fins (couteau, spatule…)
    n,lab,st,_=cv2.connectedComponentsWithStats(br)
    m=np.zeros_like(br)
    for i in range(1,n):
        x,y,w,h,area=st[i]
        if area<1500 or area>30000 or w>320 or h>260 or x==0 or y==0 or x+w>=v.shape[1] or y+h>=v.shape[0]: continue
        comp=(lab==i).astype(np.uint8)
        if np.percentile(v[comp>0],95)<.88: continue
        ring=cv2.dilate(comp,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(61,61)))-cv2.dilate(comp,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(25,25)))
        rv=v[ring>0]
        if rv.size and np.median(rv)<.50 and np.mean(rv<.35)>.12: m|=comp
    m=cv2.dilate(m,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(55,55)))
    return cv2.GaussianBlur(m.astype(np.float32),(0,0),13)
def fix(im):
    a=np.asarray(im.convert('RGB')).astype(np.float32)/255
    R,G,B=a[...,0],a[...,1],a[...,2]
    v=a.max(2);sat=(v-a.min(2))/np.maximum(v,1e-3)
    # traces d'éponge : gris froids sur fond noir, uniquement dans les zones sombres (plaque)
    w=ramp(v,.12,.19)*(1-ramp(v,.80,.92))*ramp(B-R,-.035,.005)*(1-ramp(sat,.26,.34))
    w=np.asarray(Image.fromarray((w*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(2))).astype(np.float32)/255
    loc=np.asarray(Image.fromarray((np.minimum(v,.45)*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(28))).astype(np.float32)/255
    w=w*(1-ramp(loc,.30,.40))
    # reflets des lampes
    w=np.maximum(w,reflets(v,sat)*(1-ramp(sat,.30,.40)))
    target=0.10+(v-0.10).clip(0)*0.06
    newv=v*(1-w)+np.minimum(v,target)*w
    out=(a*(newv/np.maximum(v,1e-3))[...,None]).clip(0,1)
    return Image.fromarray((out*255+.5).astype(np.uint8))
if __name__=='__main__':
    for f in sys.argv[1:]: fix(Image.open(f)).save(f.replace('.png','_n.png'))
