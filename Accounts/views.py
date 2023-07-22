from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import RegisterationSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['POST',])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout_view(request):
	'''Related Default DRF token authentication - Can be deleted'''
	if request.user.is_authenticated:
		request.user.auth_token.delete()
		return Response(status=status.HTTP_200_OK)
	return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST',])
def registeration_view(request):
	'''Related Default DRF token authentication - Can be deleted'''
	data = {}
	serializer = RegisterationSerializer(data = request.data)
	if serializer.is_valid():
		user = serializer.save()
		token = Token.objects.get(user_id = user.pk).key
		data.update({'username':user.username, 'token':token})
	else:
		data = serializer.errors

	return Response(data)



