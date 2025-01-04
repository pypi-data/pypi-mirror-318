from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns +=[
                path('somethings/', views.something_list, name='something_list'),
                path('somethings/new/', views.process_something_form, name='something_create'),
                path('somethings/<int:pk>/', views.something_detail, name='something_detail'),
                path('somethings/<int:pk>/edit/', views.process_something_form, name='something_update'),
                path('somethings/<int:pk>/delete/', views.something_delete, name='something_delete'),
            ]