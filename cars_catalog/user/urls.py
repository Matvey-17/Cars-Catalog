from django.urls import path
from user.forms import CustomLoginView
from user.views import logout, registration

app_name = 'user'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('registration/', registration, name='registration')
]
