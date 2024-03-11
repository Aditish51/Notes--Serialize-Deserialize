from django.shortcuts import render

# Create your views here.
# notes/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
import msgpack
from .models import Note
from .forms import NoteForm, FileUploadForm
def note_list(request):
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()

    return render(request, 'notes/add_note.html', {'form': form})

def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect('note_list')

def serialize_notes(request):
    notes = list(Note.objects.values())
    serialized_data = msgpack.packb(notes)
    response = HttpResponse(serialized_data, content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename=notes.msgpack'
    return response

def deserialize_notes(request):
    notes = []

    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)

        if form.is_valid():
            # Handle the uploaded file
            msgpack_file = request.FILES['msgpack_file']
            try:
                notes_data = msgpack.loads(msgpack_file.read(), raw=False)
                notes = [NoteForm(note) for note in notes_data]
            except msgpack.ExtraData:
                # Display the error to the user
                form.add_error('msgpack_file', 'Invalid MsgPack file. Please upload a valid file.')

    else:
        form = FileUploadForm()

    return render(request, 'notes/deserialize_notes.html', {'form': form, 'notes': notes})