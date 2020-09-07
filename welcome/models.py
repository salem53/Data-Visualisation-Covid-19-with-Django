from django.db import models


# Create your models here.
class Feedback(models.Model):
    firstname = models.CharField(max_length=200, help_text="Name of the sender")
    lasttname = models.CharField(max_length=200, help_text="Last Name of the sender")
    areacode = models.CharField(max_length=200, help_text="Last Name of the sender")
    telnum = models.CharField(max_length=200, help_text="Last Name of the sender")
    emailid = models.EmailField(max_length=200)
    feedback = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name + "-" +  self.email
