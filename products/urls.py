from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('', views.prod_list, name='all_products'),
    path('<uuid:category_id>/', views.prod_list, name='products_by_category'),
    path('<uuid:category_id>/<uuid:product_id>/',
         views.product_detail, name='product_detail'),
    path('product/new/', views.ProductCreateView.as_view(), name='product_new'),
    path('product/<uuid:pk>/edit/',
         views.ProductUpdateView.as_view(), name='product_edit'),
    path('product/<uuid:pk>/delete/',
         views.ProductDeleteView.as_view(), name='product_delete')
]
