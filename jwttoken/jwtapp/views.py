from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, token
from .serializers import UserSerializer, TokenSerializer


def welcome(request):
    return HttpResponse("Welcome To Encode and decode token")


@api_view(['POST'])
def create_user(request):
    import jwt
    import json
    from datetime import datetime, timedelta
    payload = request.data
    print(payload)
    more_payload = {
        'sub': '1234567890',
        'name': payload['user_id'],
        'user_name': payload['user_name'],
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=10),
        'aud': 'Girinagar'
    }
    print(more_payload)
    secret_key = "VISHWAS-Application-SAFETY"
    token = jwt.encode(more_payload, secret_key, algorithm="HS256")
    print(token)
    result = json.loads(json.dumps({"json_token": token}))
    serializer = UserSerializer(data=payload)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    serializer1 = TokenSerializer(data=result)
    if serializer1.is_valid(raise_exception=True):
        print('dfghjkdjhbfg')
        serializer1.save()
    final_data = {
        'user_data': serializer.data,
        "Encoded Token": token,
    }
    return Response(final_data)


@api_view(['GET'])
def userList(request):
    details = User.objects.all()
    serializer = UserSerializer(details, many=True)
    return Response(serializer.data)
