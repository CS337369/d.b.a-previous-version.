import board
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from graphene_django.views import GraphQLView
# from .schema import schema
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('board.urls')),
    path('', include('album.urls')),
    # path('graphql', 
    #     csrf_exempt(GraphQLView.as_view(
    #     graphiql = True,
    #     schema = schema
    #     ))),
]
