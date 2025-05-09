from django import forms
from .models import *


class NotesForm(forms.ModelForm):
    note_title = forms.CharField(
        label="Title:",
    )
    note_body = forms.CharField(
        label="Content:",
        widget=forms.Textarea(),
    )

    class Meta:
        model = Notes
        fields = [
            "note_title",
            "note_body",
        ]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields["user"].initial = self.user
