from django.contrib import admin
from django.urls import path, include

from app.urls import productpatters

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include(productpatters))
]
