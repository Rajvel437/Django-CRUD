from django.urls import path

from . import views

urlpatterns=[
    path('',views.home,name="Home"),
    path('insert',views.insert,name="insert"),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.delete),
]