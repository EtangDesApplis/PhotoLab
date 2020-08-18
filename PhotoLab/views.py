from django.http import HttpResponse
from django.shortcuts import render

from django.core.files.storage import FileSystemStorage
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.staticfiles.finders import find

from PhotoLab.PhotoPrinter import *
from PhotoLab.PhotoCreator import *

def urlToPathOfStaticFile(url):
    return find(url.replace("/static/",""))

def urlToPathOfMediaFile(url):
    fs=FileSystemStorage()
    return fs.path(url.replace("/media/",""))

def creation(request):
    context={}
    if request.method == 'POST':
        if 'image' in request.FILES:
            # this is the post to upload image 
            uploadedFile=request.FILES['image']
            print("[LOG]: Uploaded image %s [%d bytes]"%(uploadedFile.name,uploadedFile.size))
            fs=FileSystemStorage()
            #print(type(uploadedFile))
            imageFile=fs.save(uploadedFile.name,uploadedFile)
            #print(imageFile)
            #print(fs.path(imageFile))
            #print(fs.path('std_FR.png'))
            
            imageURL=fs.url(imageFile)
            print("[LOG]: Image is stored at: %s"%(imageURL))

            context['urlInputImg']=imageURL
        else:
            #this is the post to create photo from image
            #print(request.POST.keys())
            fs=FileSystemStorage()
            print("[LOG]: image to crop: %s"%(request.POST["imageSrc"])) # height=300
            print("[LOG]: format to apply: %s"%(request.POST["photoformat"]))
            print("[LOG]: posX value is: %s"%(request.POST["posX"]))
            print("[LOG]: posY value is: %s"%(request.POST["posY"]))
            print("[LOG]: posZ value is: %s"%(request.POST["posZ"]))# z*3 is the height in pixel of photo frame
            #print(find("images/std_FR.png"))
            PC=PhotoCreator()
            photoFile=PC.process(urlToPathOfMediaFile(request.POST["imageSrc"]), \
                                 urlToPathOfStaticFile(request.POST["photoformat"]), \
                                 int(request.POST["posX"]), \
                                 int(request.POST["posY"]), \
                                 int(request.POST["posZ"])*3, \
                                 300 \
                                 )

            photoURL=fs.url(photoFile.split("/")[-1])
            print("[LOG]: Photo is stored at: %s"%(photoURL))
            context['urlOutImg']=photoURL

    return render(request,'creation.html',context)

def about(request):
    return render(request,'about.html')

def printing(request):
    context={}
    if request.method == 'POST':
        uploadedFile=request.FILES['image']
        print("[LOG]: Uploaded image %s [%d bytes]"%(uploadedFile.name,uploadedFile.size))
        fs=FileSystemStorage()
        #print(type(uploadedFile))
        imageFile=fs.save(uploadedFile.name,uploadedFile)
        #print(imageFile)
        imageURL=fs.url(imageFile)
        print("[LOG]: Image is stored at: %s"%(imageURL))
        print("[LOG]: Image format: %s"%(request.POST["imageFormat"]))
        print("[LOG]: Photo format: %s"%(request.POST["photoFormat"]))
        
        #----------
        #process 
        #----------

        PP=PhotoPrinter()

        #set input format
        tmp=list(map(float,request.POST["imageFormat"].split('x')))
        PP.setInput(fs.path(imageFile),tmp[0],tmp[1])

        #set output format
        tmp=list(map(float,request.POST["photoFormat"].split('x')))
        PP.setOutput(tmp[0],tmp[1])

        #cast image into photo
        photoFile=PP.process()

        #send URL to display on web page
        photoURL=fs.url(photoFile.split("/")[-1])
        print("[LOG]: Photo is stored at: %s"%(photoURL))
        context['url']=photoURL

    return render(request,'printing.html',context)