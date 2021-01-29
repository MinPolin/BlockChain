from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.blocks, name = 'blocks' ),
    path('<int:height>/', views.one_block,name='one_block'),

]
