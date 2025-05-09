from django.db import models
from django.utils import timezone
from apps.users.models import CustomUser


# Create your models here.
class Notes(models.Model):
    note_title = models.CharField(max_length=150, unique=True)
    note_body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="Author",
    )

    def __str__(self):
        return self.note_title
