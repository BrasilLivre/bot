from django.conf.urls import include, url
from .views import BotView
urlpatterns = [
                  url(r'^bot/?$', BotView.as_view()) 
               ]
