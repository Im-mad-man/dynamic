from app import views
from django.urls import path

app_name='app'


urlpatterns=[

path('',views.IndexView.as_view()),
path('',views.ItemListView.as_view(),name='list'),
path('',views.ItemDetailView.as_view(),name='detail'),



]
