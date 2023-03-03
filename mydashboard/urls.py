from django.urls import path
from .import views

urlpatterns =[
   path('',views.index, name='dashboard-index'),
   path('home',views.index, name='dashboard-index'),
   path('kleve',views.kleve, name='dashboard-kleve'),
   path('wesel',views.wesel, name='dashboard-wesel'),
   path('visual',views.visual, name='dashboard-visulize_wesel'),
   path('visualKleve',views.visualKleve, name='dashboard-visulize'),
    path('map',views.map, name='dashboard-map'),
]