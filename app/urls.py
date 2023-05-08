from django.urls import path

from app.views import prod

productpatters = [
    path('', prod)
]
