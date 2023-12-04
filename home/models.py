from django.db import models

# Create your models here.
class Messages(models.Model):
    """
    model for storing user's inquiry
    when they fill in the form
    via contact page. This is for both registered and
    unregistered users
    """
    class Meta:
        verbose_name_plural = 'Messages'
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name