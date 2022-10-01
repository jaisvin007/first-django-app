from django.urls import path
from . import views
from .views import ProductApi

urlpatterns = [
    path('', views.hello_world),
    path('product/', views.product),
    path('product-classbased/', ProductApi.as_view()),
 ]
