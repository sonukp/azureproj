from django.db import models
import uuid
# Create your models here.


class QueueModel(models.Model):
    q_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message = models.CharField(max_length=3000)
    created = models.DateTimeField(auto_now=True)
    mgs_id = models.CharField(max_length=50, blank=True)
    status = models.CharField(blank=None, max_length=30)

    def __str__(self):
        return self.message
