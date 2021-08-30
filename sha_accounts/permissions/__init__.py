from rest_framework.permissions import BasePermission
from djrest_wrapper.exceptions.apis import PemissionDeniedExp
# extends rest framework base permission class


class BasePerm(BasePermission):
    def has_permission(self, request, view):
        self.query_name = self.__class__.__name__.lower()
        try:
            if request.user.permissions.get(name=self.query_name):
                return True
            else:
                raise PemissionDeniedExp('Permission Denied')
        except AttributeError as e:
            raise PemissionDeniedExp('Permission Denied')

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True


class IsAuthenticated(BasePerm):
    pass
