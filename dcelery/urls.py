from django.conf.urls import url,include
import dcelery.views

urlpatterns = [
    url(r'^celerytest/$', dcelery.views.celeryTest,name='celerytest' ),
]