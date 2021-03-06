# -*- coding: utf-8 -*-
from ylimg.ylimgTool import *
from yllab import *
u'''
使用`ifTest([funName]) or 0:`来判断是否执行测试
这样 在测试过程中可以在iPython 查看每一个变量
'''
imgGlob = u'/media/dl/60B49345B4931D1A1/IMPORTANT_dataForHome/salDataset/SalBenchmark-master/Data/HKU-IS/Imgs/*.jpg'
#imgGlob = ''
jpg,png='imgForTest/0004.jpg','imgForTest/0004.png'
img,gt = imread(jpg),imread(png)
gt = gt>0
re = gt.copy()
# 多分类数据
gtm = np.zeros(img.shape[:2],img.dtype)
gtm[gt>.5] =1 
gtm[15:55] = 2
gtm[250:265] = 3
rem = gtm.copy()
rem[:,10:50] = 0
rem[:,100:150] = 1
rem[:,200:250] = 2
rem[:,300:350] = 3
colors = npa([[.5,.5,.5],[1,0,0],[0,1,0],[0,0,1],])
rec,gtc = (labelToColor(rem,colors),labelToColor(gtm,colors))

def ifTest(fun):
    shouldTest = fun is tests or (isinstance(tests,list) and fun in tests) or TEST_ALL 
    if shouldTest:
        try:
            pred('Test:'+ fun.__name__);log('Type:'+ str(type(fun)))
            log('Doc :'+ fun.__doc__)
        except Exception:
            pass
    return shouldTest

TEST_ALL = True
#TEST_ALL = False

testFun = None
tests = [testFun]

#tests = generateBigImgForPaper
if ifTest(generateBigImgForPaper):
    gtmod = classDiff(rem,gtm,colors)
    remod = classDiff(rem,gtm,colors,reMod=True)
    remn,gtmn = map(normalizing,(rem,gtm))
    imgMa = ((gt,remn,gtmn,remn,),
            (re,rec,gtc,rec,),
            (img,gtmod,remod,gtmod,))
    generateBigImgForPaper(imgMa,lengh=1980,border=20,saveName='')

#tests = ndarrayToImgLists
if ifTest(ndarrayToImgLists):
    re = npa-[[gt,gt],[gt,gt]]
    tree(ndarrayToImgLists(re))
    gt = img
    re = npa-[[gt,gt],[gt,gt]]
    tree(ndarrayToImgLists(re))
    tree(ndarrayToImgLists(gt))
    
#tests = show
if ifTest(show):
    re = [{1:rec,2:gtc},
          [(gt,)],
          [img,gt],
          gt,gtm
          ]
    show(re)


#tests = tree
if ifTest(tree):
    re = [{'a':1,'b':3},
          [],
          [5,6,(gt,'string! ^_^')],
          [img,gt],
          gt,
          ]
    se = re   
    tree(se)



#tests = treem
if ifTest(treem):
    import yllab
    treem(os,[type],2)
#tests = shows
if ifTest(shows):
#    shows(jpg,png,rec,gtc)
    shows(jpg,png,rec,gtc,rem*5,gtm*5)
    
#tests = getShapes
if ifTest(getShapes) and len(glob(imgGlob)):
    with timeit():
        shapes = getShapes(imgGlob)
        
#tests = autoSegmentWholeImg
if ifTest(autoSegmentWholeImg):
    img = da.astronaut()
    hh,ww = 256,256
    hh,ww = 128,128
    resoult = autoSegmentWholeImg(img,(hh,ww),lambda x:x.mean(2)*getWeightCore(hh,ww),
                                  step=100,weightCore='gauss')
    show(resoult)

#tests = plot3dSurface
if ifTest(plot3dSurface):
    with timeit():
        hh,ww = 256,256
        print(u'seta=2高斯分布')
        core = getWeightCore(hh,ww,seta=2)
        plot3dSurface(core)
        print(u'距离分布')
        core = getWeightCore(hh,ww,lambda i,j:((i*1./hh-.5)**2+(j*1./ww-.5)**2)**.5)
        plot3dSurface(core)
        
#tests = labelToColor
if ifTest(labelToColor):
    show(rem,labelToColor(rem,includeBackGround=1))
    
#tests = getDefaultColorList
if ifTest(getDefaultColorList):
    toi = lambda(p):(npa([[p]*4]*4))*1.
    colorNum=3
    includeBackGround=-1
    colors = getDefaultColorList(colorNum,includeBackGround)
    print colorNum,len(colors)
    show -map(toi,colors)
if __name__ == '__main__':
    pass




