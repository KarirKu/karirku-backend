import uuid
from django.db import models
from user.models import User

class CeritaAlumni(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    judul = models.CharField(max_length=100)
    isi = models.TextField()
    alumni = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.judul