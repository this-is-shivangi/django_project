from django.urls import path
from . import views
app_name = 'advblog'

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<int:slug>/',views.post_detail,name='post_detail')
]