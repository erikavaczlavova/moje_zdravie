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
            entries = Test.objects.filter(user=request.GET['user_id'], type=request.GET['type'])
            responses = {
                'items': []
            }
            if entries:
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
            else:
                return HttpResponseNotFound("Error: 404 Not Found")
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
            user = User.objects.get(id=body['user_id'])
            new = Test(user=user, date=body['date'], location=body['location'], type=body['type'])
            new.save()
            return HttpResponse("Succesfully saved")
        except:
            return HttpResponseBadRequest("Bad request")

@csrf_exempt
def vaccine(request):
    if request.method == "GET":
        try:
            entries = Vaccine.objects.filter(user=request.GET['user_id'])
            responses = {
                'items': []
            }
            if entries:
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
            else:
                return HttpResponseNotFound("Error: 404 Not Found")
        except:
            return HttpResponseNotFound("Error: 404 Not Found")

    elif request.method == "PUT":
        try:
            body = json.loads(request.body)
            user = User.objects.get(id=body['user_id'])
            new = Vaccine(user=user, date=body['date'], dose=body['dose'], location=body['location'], name=body['name'],doctor=body['doctor'])
            new.save()
            return HttpResponse("Succesfully saved")
        except:
            return HttpResponseBadRequest("Bad request")

@csrf_exempt
def passport(request):
    if request.method == "GET":
        if True:
            print("aaa")
            entries = Passport.objects.filter(user_id=request.GET['user_id'])
            responses = {
                'items': []
            }
            print(entries, "aaa")
            if entries:
                for entry in entries:
                    response = {}
                    response['id'] = entry.id
                    response['user_id'] = entry.user_id
                    response['vaccine_id'] = entry.vaccine.id
                    response['date'] = entry.vaccine.date
                    response['dose'] = entry.vaccine.dose
                    response['name'] = entry.vaccine.name
                    responses['items'].append(response)
                return JsonResponse(responses)
            else:
                return HttpResponseNotFound("Error: 404 Not Found")
        else:
            return HttpResponseNotFound("Error: 404 Not Found")

@csrf_exempt
def user(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            entry = User.objects.get(id=body['id'])
            entry.name = body['name']
            entry.password = body['password']
            entry.birthnum = body['birthnum']
            entry.birthdate = body['birthdate']
            entry.weight = body['weight']
            entry.height = body['height']
            entry.save()
            return HttpResponse("Succesfully saved")
        except:
            return HttpResponseNotFound("Error: 404 Not Found")

    elif request.method == "GET":
        try:
            entry = User.objects.get(id=request.GET['id'])
            response = {}
            response['id'] = entry.id
            response['name'] = entry.name
            response['birthnum'] = entry.birthnum
            response['birthdate'] = entry.birthdate
            response['password'] = entry.password
            response['weight'] = entry.weight
            response['height'] = entry.height
            return JsonResponse(response)
        except:
            return HttpResponseNotFound("Error: 404 Not Found")
