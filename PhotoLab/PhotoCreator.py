from PIL import Image

class PhotoCreator:
  def __init__(self):
    pass
  
  def process(self,inputFile,formatFile,pX0,pY0,dY,Yref):
    inputImg=Image.open(inputFile)
    formatImg=Image.open(formatFile)
    X0=inputImg.height/Yref*pX0
    Y0=inputImg.height/Yref*pY0
    DY=inputImg.height/Yref*dY
    DX=inputImg.height/Yref*(formatImg.width*dY/formatImg.height)

    imageType="."+inputFile.split('.')[-1]
    imageFile=inputFile.replace(imageType,"_croped"+imageType)
    inputImg.crop((X0,Y0,X0+DX,Y0+DY)).save(imageFile,quality=95)
    return imageFile


if __name__=="__main__":
  pass