from django.conf.urls import url, include
#from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^$', post_tweet),
    url(r'^thankyou/', thank_you),
    url(r'^edit/(?P<tweet_id>\d+)', post_tweet),
]
