from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from users.models import User
from users.serializers import UserSerializer

@csrf_exempt
def users_api(request, id=None):
    if request.method == 'GET':
        users = list(User.objects.all())  
        users_serialized = UserSerializer(users, many=True)
        return JsonResponse(users_serialized.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        users_serialized = UserSerializer(data=user_data)
        if users_serialized.is_valid():
            users_serialized.save()
            return JsonResponse({"message": "User data added successfully."}, safe=False)
        return JsonResponse({"error": "Failed to add user."}, safe=False)

    elif request.method == 'PUT':
        user_put_data = JSONParser().parse(request)

        if not id:
            return JsonResponse({"error": "User ID is required for update."}, safe=False, status=400)

        try:
            user = User.objects.get(id=id) 
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found."}, safe=False, status=404)

        updated_data = {**user.to_mongo().to_dict(), **user_put_data}

        users_serialized = UserSerializer(user, data=updated_data, partial=True)
        if users_serialized.is_valid():
            users_serialized.save()
            return JsonResponse({"message": "User data updated successfully."}, safe=False)

        return JsonResponse({"error": "Failed to update user."}, safe=False)



    elif request.method == 'DELETE':
        try:
            user = User.objects.get(id=id) 
            user.delete()
            return JsonResponse({"message": "User deleted successfully."}, safe=False)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found."}, safe=False, status=404)
