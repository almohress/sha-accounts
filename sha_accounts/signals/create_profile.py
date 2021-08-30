from django.dispatch import receiver
from django.db.models.signals import post_save
from ..models.user_models import User
from ..models.profile_models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance: User, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
