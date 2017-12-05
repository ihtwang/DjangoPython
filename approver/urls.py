from django.conf.urls import url, include
#from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^$', list_tweets),
    url(r'^review/(?P<tweet_id>\d+)$', review_tweet),
    ]