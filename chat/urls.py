from django.conf.urls import url,include
import chat.views

urlpatterns = [
    url(r'^chatroom/$', chat.views.chatroom,name='chatroom' ),
]