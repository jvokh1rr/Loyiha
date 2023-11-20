from django.urls import path
from home import views


urlpatterns = [
    path('', views.pro, name='pro'),
    path('first_page/', views.first_page, name='first_page'),
    path('post_jonatish/', views.post_jonatish, name='post_jonatish'),
    path('addAuto/', views.addAuto, name='addAuto'),
    path('edit_auto/<int:id>/', views.edit_auto, name='edit_auto'),
    path('delate_auto/<int:id>/', views.delate_auto, name='delate_auto'),
    ####################################################################
    path('product/', views.product, name='product'),
    path('carousel/', views.carousel, name='carousel'),
    path('ckeditorr/', views.ckeditorr, name='ckeditorr'),
    path('example/', views.example, name='example'),
]
##############################################################################
