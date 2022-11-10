from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('<int:brand_id>', mainapp.brand, name='index'),
    path('collection/<int:pk>', mainapp.collection_view, name='collection')
]
