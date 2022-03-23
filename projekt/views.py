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
            entries = Test.objects.filter(user_id=request.GET['user_id'], type=request.GET['type'])
            responses = {
                'items': []
            }
            for entry in entries:
                response = {}
                response['id'] = entry.id
                response['user_id'] = entry.user_id
                response['date'] = entry.date
                response['result'] = entry.result
                response['location'] = entry.location
                response['type'] = entry.type
                responses['items'].append(response)
            return JsonResponse(responses)
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

@csrf_exempt
def vaccine(request):
    if request.method == "GET":
        try:
            entries = Vaccine.objects.filter(user_id=request.GET['user_id'])
            responses = {
                'items': []
            }
            for entry in entries:
                response = {}
                response['id'] = entry.id
                response['user_id'] = entry.user_id
                response['date'] = entry.date
                response['dose'] = entry.dose
                response['location'] = entry.location
                response['name'] = entry.name
                response['doctor'] = entry.doctor
                responses['items'].append(response)
            return JsonResponse(responses)
        except:
           return HttpResponseNotFound("Error: 404 Not Found")

    elif request.method == "PUT":
        try:
            body = json.loads(request.body)
            new = Vaccine(user_id=body['user_id'], date=body['date'], dose=body['dose'], location=body['location'], name=body['name'],doctor=body['doctor'])
            new.save()
            return HttpResponse("Succesfully saved")
        except:
            return HttpResponseBadRequest("Bad request")