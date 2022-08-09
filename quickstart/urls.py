from django.urls import include, path
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoriesViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'cart', views.CartViewSet)
router.register(r'cartItem', views.CartItemViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]