from django.conf.urls import url
from . import views

app_name = "cases"

urlpatterns = [
    url(
        regex=r'^all/$',
        view=views.ListAllCases.as_view(),
        name='all_cases'
    )
]