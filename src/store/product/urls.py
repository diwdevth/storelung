from django.urls import path
from .views import Home, About, APIAllproduct, APIProduct
urlpatterns = [
    path('', Home, name='home-page'),
    path('about/', About, name='about-page'),
    path('apiproduct/', APIAllproduct, name='api-product'),
    path('apisingle/<int:pk>/', APIProduct)

]