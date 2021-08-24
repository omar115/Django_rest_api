from django.db import models
from django.conf import settings

# Create your models here.

def upload_status_image(instance, filename):
    return "uploads/{user}/{filename}".format(user=instance.user, filename=filename)

class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # taking the default user model
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to = upload_status_image,null=True, blank=True)
    updated = models.DateTimeField(auto_now=True) # when the status is updated
    created = models.DateTimeField(auto_now_add=True) # when the status is created

    # default return of a status
    # pura status jeta create holo ota kivabe dekhabe jate access kora jai
    def __str__(self):
        return str(self.content)[0:30]  # slice and take first 30 characters
    
    # how the admin panel shows you the name
    # admin panel e column name ta ki dekhabe
    class Meta:
        verbose_name_plural = "Status List"