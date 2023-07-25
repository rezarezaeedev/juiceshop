from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status



@api_view(['POST',])
def registeration_view(request):
	data = {}
	serializer = RegisterationSerializer(data = request.data)
	if serializer.is_valid():
		user = serializer.save()
		refresh = RefreshToken.for_user(user)
		data.update({'username':user.username, 'token':{'refresh':str(refresh), 'access':str(refresh.access_token),}})
	else:
		data = serializer.errors

	return Response(data, status=status.HTTP_201_CREATED)
