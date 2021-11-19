from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

from django import forms
#
# from uploads.core.models import Document

#class DocumentForm(forms.ModelForm):
#    class Meta:
#        model = Document
#        fields = ('description', 'document', )
