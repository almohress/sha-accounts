from django.contrib.auth.models import BaseUserManager
from ..models import Permission


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        auth_perm = Permission.objects.get_or_create(name='isauthenticated')
        user.permissions.add(auth_perm[0].id)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username, email=email, password=password)
        admin_perm = Permission.objects.get_or_create(name='isadmin')
        user.permissions.add(admin_perm[0].id)
        user.save(using=self._db)
        return user
