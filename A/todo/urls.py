from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todos', views.TodoViewSet)

urlpatterns = router.urls