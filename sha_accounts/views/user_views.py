from djrest_wrapper.interfaces import BaseViewSet
from ..models.user_models import User
from ..serializers.user_serializers import UserSignUpRequest, UserSignUpResponse


class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_action_classes = {
        'create': {
            'req': UserSignUpRequest,
            'res': UserSignUpResponse,
        },
        'retrieve': {
            'res': UserSignUpResponse,
        },
        'signin': {
            'req': UserSignInRequest,
            'res': UserSignInResponse,
        }
    }
