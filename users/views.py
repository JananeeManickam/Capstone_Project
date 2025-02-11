from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from users.models import User
from users.serializers import UserSerializer


@csrf_exempt
def users_api(request, id=0):
    if request.method == 'GET':
        users = User.objects.all()
        users_serialized = UserSerializer(users, many=True)
        return JsonResponse(users_serialized.data, safe=False)
    
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        users_serialized = UserSerializer(data=user_data)
        if users_serialized.is_valid():
            users_serialized.save()
            return JsonResponse("User data added successfully...", safe=False)
        return JsonResponse("Failed to add user.", safe=False)
    
    elif request.method == 'PUT':
        user_put_data = JSONParser().parse(request)
        user = User.objects.get(_id = user_put_data['_id'])
        users_serialized = UserSerializer(user, data=user_put_data)
        if users_serialized.is_valid():
            users_serialized.save()
            return JsonResponse("User data updated successfully...", safe=False)
        return JsonResponse("Failed to update user.", safe=False)
    
    elif request.method == 'DELETE':
        user = User.objects.get(_id = user_put_data['_id'])
        user.delete()
        return JsonResponse("User deleted successfully...", safe=False)