from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Gift(models.Model):
    requestor = models.ForeignKey(User, 
                on_delete=models.CASCADE, 
                related_name='requestor')

    description = models.CharField(max_length=200)
    gift_link = models.URLField(max_length=200, null=True, blank=True)
    gift_claimed = models.BooleanField(default=False)
    gift_claimed_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    email = models.CharField(max_length=200, null=True)
    # image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username
