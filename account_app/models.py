

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# this is not used for regitering user it used for profile of the use when user wants to complete his or her
# porfile like address image and phone_number or email 
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_photo = models.ImageField(upload_to='Images/user_profile_images', null=True,blank=True)
    address = models.TextField(max_length=1000,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.user.username
    

@receiver(post_save, sender = User )
def create_or_update_user_profile(sender , instance ,created,**kwargs):
	if created:
		UserProfile.objects.create(user = instance)
		# model name 					user of db we made

def save_profile(sender, instance, **kwargs):
  instance.profile.save()
