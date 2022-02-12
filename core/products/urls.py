from importlib.resources import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    ProductViewList, ProductDetailView ,
    CategoryView
)
from django.urls import path

urlpatterns = [ 
    path('', ProductViewList.as_view(), name='product_list'),
    path('product/<slug>/', ProductDetailView.as_view(), name='product'),
    path('category/<slug:slug>/' ,CategoryView.as_view(), name="category" ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)