from django.db import models

# Create your models here.
class Posts(models.Model):
    heading = models.CharField(max_length=25, null=False)
    sub_heading = models.CharField(max_length=25, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading

