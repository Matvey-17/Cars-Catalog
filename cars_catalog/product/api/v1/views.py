from product.api.v1.serializers import (ListCarSerializer, CarSerializer,
                                        ListCommentSerializer, CommentSerializer)
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from product.models import Car, Comment
from rest_framework.response import Response


class ApiViewCars(APIView):
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.request.method in ('POST', 'PUT', 'DELETE'):
            return [IsAuthenticated()]
        return [AllowAny()]

    def get(self, request, car_id=None):
        if not car_id:
            cars = Car.objects.select_related('owner').all()
            serializer = ListCarSerializer(cars, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            try:
                car = Car.objects.select_related('owner').get(id=car_id)
                serializer = ListCarSerializer(car)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Car.DoesNotExist:
                return Response({'detail': 'Запись не найдена'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = CarSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, car_id=None):
        if not car_id:
            return Response({'detail': 'Метод не разрешен'}, status=status.HTTP_403_FORBIDDEN)
        try:
            car = Car.objects.get(id=car_id, owner=request.user)
        except Car.DoesNotExist:
            return Response({'detail': 'Запись не найдена'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(car, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, car_id=None):
        if not car_id:
            return Response({'detail': 'Метод не разрешен'}, status=status.HTTP_403_FORBIDDEN)
        try:
            car = Car.objects.get(id=car_id, owner=request.user)
            car.delete()
            return Response({'detail': 'Автомобиль успешно удален'}, status=status.HTTP_204_NO_CONTENT)
        except Car.DoesNotExist:
            return Response({'detail': 'Автомобиль не найден'}, status=status.HTTP_404_NOT_FOUND)


class ApiViewComments(APIView):
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]

    def get(self, request, car_id):
        comments = Comment.objects.select_related('car', 'author').filter(car_id=car_id)
        if comments.exists():
            serializer = ListCommentSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'Комментарий не найден'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, car_id):
        try:
            car = Car.objects.get(id=car_id)
        except Car.DoesNotExist:
            return Response({'detail': 'Запись не найдена'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializer(data=request.data, context={'request': request, 'car': car})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
