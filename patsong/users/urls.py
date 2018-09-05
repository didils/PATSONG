from django.conf.urls import url
from . import views

app_name = "users"

urlpatterns = [
    url(
        regex=r'^(?P<username>\w+)/password/$',
        view=views.ChangePassword.as_view(),
        name='change'
    ),
    url(
        regex=r'^login/facebook/$',
        view=views.FacebookLogin.as_view(),
        name='fb_login'
    ),
]