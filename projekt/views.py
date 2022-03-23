from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, QueryDict, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json
from projekt.models import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def test(request):
    if request.method == "GET":
        try:
            entry = Test.objects.get(user_id=request.GET['user_id'])
            response = {}
            response['id'] = entry.id
            response['user_id'] = entry.user_id
            response['date'] = entry.date
            response['result'] = entry.result
            response['location'] = entry.location
            response['type'] = entry.type
            return JsonResponse(response)
        except:
            return HttpResponseNotFound("Error: 404 Not Found")

    elif request.method == "DELETE":
        try:
            entry = Test.objects.get(id=request.GET['id'])
            print(entry.id)
            entry.delete()
            return HttpResponse("Deleted")
        except:
            return HttpResponseNotFound("Error: 404 Not Found")

    elif request.method == "PUT":
        try:
            body = json.loads(request.body)
            new = Test(user_id=body['user_id'], date=body['date'], location=body['location'], type=body['type'], result=False)
            new.save()
            return HttpResponse("Succesfully saved")
        except:
            return HttpResponseBadRequest("Bad request")
