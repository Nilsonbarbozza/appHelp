from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,  permission_classes
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated



@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Usuário criado com sucesso"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)
