from django.urls import path
from .views import combined_view # Убедитесь, что combined_view импортирована

urlpatterns = [
    path('dashboard/', combined_view, name='registration'),  # передайте функцию без вызова

]
