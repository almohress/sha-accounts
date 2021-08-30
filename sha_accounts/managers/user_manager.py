from django.contrib.auth.models import BaseUserManager
from ..models import Permission


class UserManager(BaseUserManager):
    def create(self, *args, **kwargs):
        new_user = super().create(*args, **kwargs)
        auth_perm = Permission.objects.get_or_create(name='isauthenticated')
        new_user.permissions.add(auth_perm[0].id)
        new_user.save(using=self._db)
        return new_user

    def create_superuser(self, username, email, password):
        user = self.create(
            username=username, email=email, password=password)
        admin_perm = Permission.objects.get_or_create(name='isadmin')
        user.permissions.add(admin_perm[0].id)
        user.save(using=self._db)
        return user
