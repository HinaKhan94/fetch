from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path(
        'order_history/<order_number>',
        views.order_history, name='order_history'
    ),
    path('my_reviews/', views.my_reviews, name='my_reviews'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path(
        'add-to-wishlist/<int:product_id>/', 
        views.add_to_wishlist, name='add_to_wishlist'
    ),
    path(
        'remove-from-wishlist/<int:wishlist_item_id>/',
        views.remove_from_wishlist, name='remove_from_wishlist'
    ),
]