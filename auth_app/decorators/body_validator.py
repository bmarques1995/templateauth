from functools import wraps
import json
from django.http import HttpRequest, JsonResponse

def validate_request_json_body(fields: list[str], accept_extra = False):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request: HttpRequest, *args, **kwargs):
            try:
                request.json_body = json.loads(request.body)
                assert_json_fields(fields, request.json_body, accept_extra=accept_extra)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'The json provided must be valid'}, status=401)
            except FieldMismatchException as e:
                return JsonResponse({'error': e.message}, status=401)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

class FieldMismatchException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def assert_json_fields(field_list: list[str], json_body: dict, accept_extra=False, throw=True) -> bool:
    # Define the required fields
    obj_field_list = []
    missing_fields = []
    for field in json_body:
        obj_field_list.append(field)
    for field in field_list:
        if field not in obj_field_list:
            missing_fields.append(field)

    # Check for missing fields
    if missing_fields:
        if throw:
            raise FieldMismatchException(f'Missing fields: {", ".join(missing_fields)}')
        else:
            return False

    # Check for extra fields
    if not accept_extra:
        extra_fields = []
        for field in obj_field_list:
            if field not in field_list:
                extra_fields.append(field)
        if extra_fields:
            if throw:
                raise FieldMismatchException(f'Extra fields: {", ".join(extra_fields)}')
            else:
                return False
    
    return True