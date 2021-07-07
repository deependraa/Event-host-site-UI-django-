from home.models import event
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('Sevent/<int:event_id>' ,views.events,name='events'),
    path('like/<int:event_id>',views.likeview,name='like_post'),
]