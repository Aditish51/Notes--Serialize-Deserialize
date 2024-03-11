# notes/urls.py
# notes/urls.py
from . import views
from django.urls import path
from .views import note_list, add_note, deserialize_notes, delete_note
from .views import serialize_notes
urlpatterns = [
    path('', note_list, name='note_list'),
    path('add/', add_note, name='add_note'),
    path('serialize_notes/', serialize_notes, name='serialize_notes'),
    path('deserialize/', deserialize_notes, name='deserialize_notes'),
    path('deserialize/', views.deserialize_notes, name='deserialize_notes'),
    path('delete/<int:note_id>/', delete_note, name='delete_note'),
]
