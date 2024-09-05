from django.urls import path
from product.views import main, get_car, add_comment, add_car, edit_car, delete_car

app_name = 'product'

urlpatterns = [
    path('main/', main, name='main'),
    path('car/<int:car_id>/', get_car, name='car'),
    path('add_comment/<int:car_id>/', add_comment, name='add_comment'),
    path('add_car/', add_car, name='add_car'),
    path('edit_car/<int:car_id>/', edit_car, name='edit_car'),
    path('delete/<int:car_id>/', delete_car, name='delete')
]
