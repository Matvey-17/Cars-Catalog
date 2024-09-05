from product.api.v1.views import ApiViewCars, ApiViewComments
from django.urls import path

app_name = 'product'

urlpatterns = [
    path('cars/', ApiViewCars.as_view(), name='cars'),
    path('cars/<int:car_id>/', ApiViewCars.as_view(), name='car'),
    path('cars/<int:car_id>/comments/', ApiViewComments.as_view(), name='comments')
]
