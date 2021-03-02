from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('addcoursetitle', views.addcoursetitle),
    path('courses/destroy/<c_id>', views.linkdest),
    path('courses/confirmdest/<c_id>', views.remove),
]