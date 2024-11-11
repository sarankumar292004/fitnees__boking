from django.urls import path
from . import views

urlpatterns = [
    path('', views.class_list, name='class_list'),  # Home page showing the class list
    path('classes/', views.class_list, name='class_list_alt'),  # Optional direct URL for classes
    path('profile/', views.public_profile, name='public_profile'),  # Public profile page
    path('book/<int:class_id>/', views.book_class, name='book_class'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('class/<int:class_id>/', views.class_detail, name='class_detail'),
]
