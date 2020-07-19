from PIL import Image

class PhotoPrinter:
  def __init__(self):
    self.background=(0, 0, 0)

  def setInput(self,imageFile,width=3.5,height=4.5):
    self.fn=imageFile
    self.input=Image.open(self.fn)
    
    #auto rotation if needed
    if (width<=height) and (self.input.width <=self.input.height):
      self.W1=width
      self.H1=height
    else:
      self.W1=height
      self.H1=width

    self.h1=self.input.height
    self.w1=self.input.width

  def setOutput(self,width=15.0,height=10.2):
    if int(height/self.H1)*int(width/self.W1) >= int(width/self.H1)*int(height/self.W1):
      self.H2=height
      self.W2=width
    else:
      self.H2=width
      self.W2=height
  
  def process(self,imageFile=None):
    self.h2=int(self.H2/self.H1*self.h1)
    self.w2=int(self.W2/self.W1*self.w1)
    Nh=int(self.H2/self.H1)
    Nw=int(self.W2/self.W1)
    dh=int((self.h2-self.h1*Nh)/(Nh+1))
    dw=int((self.w2-self.w1*Nw)/(Nw+1))
    tmp=Image.new('RGB', (self.w2, self.h2), color = self.background)
    self.output=tmp.copy()
    #fill output image by replicas of input image
    for i in range(Nw):
      for j in range(Nh):
        self.output.paste(self.input,(dw+(self.w1+dw)*(i),dh+(self.h1+dh)*(j)))
    #store result into file
    if imageFile==None:
      imageType="."+self.fn.split('.')[-1]
      imageFile=self.fn.replace(imageType,"_%dx%d"%(int(self.W2),int(self.H2))+imageType)
    self.output.save(imageFile,quality=95)

    #this one is useful for Django file serving
    return imageFile

if __name__=="__main__":
  PP=PhotoPrinter()
  #input photo 3.5cm x 4.5cm
  PP.setInput("photo_FR.png",3.5,4.5)
  #set output format 15cm x 10.2cm
  PP.setOutput(15.0,10.2)
  PP.process()