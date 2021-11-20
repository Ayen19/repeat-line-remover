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
    context_title= {
        'unprocessed_text':"Unprocessed Text",
        'processed_text':"Processed Text",
    }



    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        p_number_of_line= len(processed_text(uploaded_file_url))
        u_number_of_line= len(unprocessed_text(uploaded_file_url))
        number_of_lines_remove = u_number_of_line - p_number_of_line

        context_file = {
            'stats':{
                "p_no":p_number_of_line,
                "u_no": u_number_of_line,
                "no_removed": number_of_lines_remove
            },
            'processed_txt': processed_text(uploaded_file_url),
            'unprocessed_txt':unprocessed_text(uploaded_file_url),
            'unprocessed_text':"Unprocessed Text",
            'processed_text':"Processed Text",
            'uploaded_file_url':uploaded_file_url
        }
        return render(request, 'duplicate_line_remover/simple_upload.html', context_file)


    return render(request, 'duplicate_line_remover/simple_upload.html', context_title)


def unprocessed_text(url):
  with open('.'+url, 'r') as file:
    return file.readlines()

def processed_text(url):
    txt_list = []
    with open('.'+url, 'r') as file:
        for item in file.readlines():
            if item in txt_list:
                pass
            else:
                txt_list.append(item)

    return txt_list