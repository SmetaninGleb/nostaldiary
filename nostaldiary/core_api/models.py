from django.db import models
from django.contrib.auth.models import User

def image_directory_path(instance, filename):
    return 'user_{0}/%Y/%m/%d'.format(instance.user_owner_id)

class ImageUploaded(models.Model):
    image = models.ImageField(upload_to=image_directory_path, null=False)
    user_owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='user_images', 
        related_query_name='user_owner'
    )
    users_allowed = models.ManyToManyField(
        User, 
        related_name='accessed_images', 
        related_query_name='users_allowed'
    )
    
class Post(models.Model):
    text = models.TextField()
    user_creator = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='created_posts',
        related_query_name='user_creator'
    )
    users_allowed = models.ManyToManyField(
        User, 
        related_name='accessed_posts', 
        related_query_name='users_allowed'
    )
    images_attached = models.ManyToManyField(ImageUploaded)
