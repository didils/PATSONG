from django.conf.urls import url
from . import views

app_name = "relations"

urlpatterns = [
    url(
        regex=r'^$',
        view=views.SaveRelations.as_view(),
        name='save_relations'
    ),
    url(
        regex=r'^search/$',
        view=views.Search.as_view(),
        name='search_relation'
    )
]