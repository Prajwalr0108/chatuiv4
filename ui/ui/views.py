from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.forms.forms import Form
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib import messages

from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
from .models import bot
#decoratror to speedup page loading
@gzip.gzip_page

# Create your views here.
#Requesting Index page and passing a value using jinja'{}'
def index(request):
    context = {
        'names' : 'FACE RECOGNITION AND OCR'}
    return render(request, 'index.html',context)


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

#Page where live web cam feed appers
def stream(request):
    return render(request, 'stream.html')

def table(request):
    
    return render(request, 'bot.html')

def chatbot(request):
    return render(request, 'chatbot.html')
#functions for the live webcam feed.
def show(request):
    try:
        
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return render(request, 'index.html')
    

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame)= self.video.read()
       
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()
        #Used to stop webcam feed
        cv2.destroyAllWindows()
  
   
    def get_frame(self):
        image= self.frame
        #imencode - for converting frames to .jpg format
        _, jpeg = cv2.imencode('.jpg', image)
        #converting .jpg to bytes
        return jpeg.tobytes()

    def update(self):
        while True:
            #creating variables to store the read frames
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        #calling get_frame function and storing function inputs in a varibale 'frame'
        frame = camera.get_frame()
        #Encoding using below pattern
        yield (b'--frame\r\n'
               b'Content-Type: image\r\n\r\n' + frame + b'\r\n\r\n')

def log(request):
    if request.method == 'POST':
        input = request.POST['input']
        output = request.POST['output']
        x = bot(input=input, output=output)
        x.save()
    
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

        

        
    







    



