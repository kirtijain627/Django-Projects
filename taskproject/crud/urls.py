from django.urls import path
from .import views

urlpatterns = [
    path('',views.add_show, name="addandshow"),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('<int:id>/', views.update_data, name="updatedata"),
    path('learndj/', views.learn_django, name="learndajngo"),

]
