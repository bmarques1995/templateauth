import json
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from auth_app.decorators.body_validator import validate_request_json_body
from auth_app.Shared.password import Password as PasswordHandler, InvalidPasswordException
from auth_app.models.user import User
from auth_app.serializers.password import PasswordSerializer
from auth_app.serializers.user import FullUserSerializer
from rest_framework import exceptions as rest_framework_exceptions

@csrf_exempt
@require_http_methods(['POST'])
@validate_request_json_body(fields=['name', 'password'], accept_extra=False)
def register_user(request: HttpRequest):
    try:    # Parse the JSON body
        request_data: dict = request.json_body
        treated_data = {
            'name': request_data['name']
        }

        password = PasswordHandler(request_data['password'])

        user: User
        user_serializer = FullUserSerializer(data= treated_data)
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()
        
        password_obj = {
            'user_idx': user.name,
            'password_hash': password.hashed_password,
        }
        password_serializer = PasswordSerializer(data = password_obj)
        if password_serializer.is_valid():
            password_serializer.save()

    except (rest_framework_exceptions.ValidationError) as e:
        return JsonResponse({'error': str(e)}, status=400)
    except (InvalidPasswordException) as e:
        return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({"msg": "Register succeeded"}, status=200)