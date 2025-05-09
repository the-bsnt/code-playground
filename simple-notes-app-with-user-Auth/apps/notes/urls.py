from django.urls import path
from .views import *

app_name = "notes"

urlpatterns = [
    path("", index, name="index"),
    path("dashboard/", dashboard, name="dashboard"),
    path("create_note/", create_note, name="create_note"),
    path("delete_note/<int:note_id>/", delete_note, name="delete_note"),
    path("edit_note/<int:note_id>", edit_note, name="edit_note"),
]
