# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files import File
from .forms  import  UploadFileForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage



def index(req):

    return render(req,"duplicate_line_remover/index.html", {})

def uploadfile(req, res):
    if req.method == 'POST':

        
        form = UploadFileForm(req.POST, req.FILES)

        return HttpResponse("THANK YOU!")
    


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')