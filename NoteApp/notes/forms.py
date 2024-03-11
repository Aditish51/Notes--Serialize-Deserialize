# notes/forms.py
from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

class FileUploadForm(forms.Form):
    msgpack_file = forms.FileField(label='Upload MsgPack File')