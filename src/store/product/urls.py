from django.urls import path
from .views import Home, About, APIAllproduct, APIProduct, api_post_allproduct
urlpatterns = [
    path('', Home, name='home-page'),
    path('about/', About, name='about-page'),
    path('apiproduct/', APIAllproduct, name='api-product'),
    path('apisingle/<int:pk>/', APIProduct),
    path('api/create', api_post_allproduct)

]