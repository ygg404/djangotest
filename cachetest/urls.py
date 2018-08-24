from django.conf.urls import url,include
import cachetest.views

urlpatterns = [
    url(r'^cache1/$', cachetest.views.cache1,name='cache1' ),
]