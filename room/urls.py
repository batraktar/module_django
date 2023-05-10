from django.contrib import admin
from django.urls import path

from app.views import Login, Registration, ProductView, Logout

urlpatterns = [
    path('', ProductView.as_view(), name='base'),
    path('admin/', admin.site.urls),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('regist/', Registration.as_view(), name='registration')
]
