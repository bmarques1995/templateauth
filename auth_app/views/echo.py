import json
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

@csrf_exempt
@require_http_methods(['POST'])
def echo_route(request: HttpRequest):
    print(request)
    json_body = json.loads(request.body)
    return JsonResponse({'msg': json_body['msg']}, status=200)