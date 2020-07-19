from django.http import HttpResponse
from django.shortcuts import render

from django.core.files.storage import FileSystemStorage

from PhotoLab.PhotoPrinter import *

def creation(request):
    return render(request,'creation.html')

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