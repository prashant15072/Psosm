from django.conf.urls import include, url
from django.contrib import admin
from complete import views
from . import views

urlpatterns = [
    url(r'^$', views.index , name="index"),
    url(r'^/follow',views.follow_users,name="follow"),
    url(r'^/dm',views.dm_users,name="dm"),
    url(r'^/tweet',views.tweet_user,name="tweet"),
    url(r'^/specific_user_tweet',views.tweet_specific_user,name="specific_user_tweet"),
    url(r'^/specific_user_follow',views.follow_specific_user,name="specific_user_follow"),
    url(r'^/specific_user_dm',views.dm_specific_user,name="specific_user_dm"),

]
