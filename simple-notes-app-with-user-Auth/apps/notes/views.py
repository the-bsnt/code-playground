from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages


def index(request):
    if request.user.is_authenticated == True:
        return redirect("notes:dashboard")
    else:
        return redirect("users:login_user")


# Notes Dashboard
@login_required
def dashboard(request):
    return render(request, "notes/dashboard.html")


@login_required
def create_note(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)  # Don't save to DB yet
            note.user = request.user  # Set the user manually
            note.save()  # Now save to DB
            messages.success(request, "New note created successfully!")
            return redirect("notes:dashboard")  # Redirect to dashboard
        else:
            messages.error(request, f"Invalid Form!!!")
    else:
        form = NotesForm()
    return render(request, "notes/create_note.html", {"form": form})


@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Notes, pk=note_id)
    note.delete()
    messages.success(request, "Note deleted successfully!")
    return redirect("notes:dashboard")


#! the defect with this view function is that we didnt validate the form. if i validate the form it will not accept the same title(without edit ) as note_title is set unique
# @login_required
# def edit_note(request, note_id):
#     note = get_object_or_404(Notes, pk=note_id)
#     if request.method == "POST":
#         note.note_title = request.POST.get("note_title")
#         note.note_body = request.POST["note_body"]
#         note.save()
#         return redirect("notes:dashboard")
#     else:
#         form = NotesForm(
#             initial={
#                 "note_title": note.note_title,
#                 "note_body": note.note_body,
#             }
#         )
#     return render(request, "notes/edit_note.html", {"form": form, "id": note.id})
@login_required
def edit_note(request, note_id):
    note = get_object_or_404(Notes, pk=note_id)
    if request.method == "POST":
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, f"Note updated successfully!")
            return redirect("notes:dashboard")
    else:
        form = NotesForm(
            initial={
                "note_title": note.note_title,
                "note_body": note.note_body,
            }
        )
    return render(request, "notes/edit_note.html", {"form": form, "id": note.id})
