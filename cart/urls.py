from django.urls import path
from .import views
urlpatterns=[
                path('cartDetails',views.cart_Details,name='cartDetails'),
                path('add/<int:product_id>/',views.add_cart,name='addcart'),
                path('dec/<int:product_id>/',views.min_cart,name='cart_decrement'),
                path('del/<int:product_id>/', views.cart_delete, name='remove'),
                path('logout',views.logout,name='logout'),

]