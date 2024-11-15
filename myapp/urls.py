from django.urls import path
from . import views

urlpatterns = [
    path('emails/', views.email_list, name="email_list"),
    path('emails/create/', views.create_email, name="create_email"),
    path('emails/update/<int:pk>/', views.update_email, name="update_email"),
    path('emails/delete/<int:pk>/', views.delete_email, name="delete_email"),
]
