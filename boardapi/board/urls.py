from . import views
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('', views.home, name="home"),
    path('board/', views.Boardapi.as_view(), name="board"),
    path('board/<int:pk>/', views.Boardapi_detail.as_view(), name="board_detail"),
    path('board/write/', views.Boardapi_writeview, name="board_write"),
    path('board/insert/', views.Boardapi_insert.as_view(), name="board_insert"),
    path('board/<int:pk>/edit/', views.Boardapi_edit.as_view(), name="board_edit"),
    path('board/<int:pk>/update/', views.Boardapi_update.as_view(), name="board_update"),
    path('board/<int:pk>/delete/', views.Boardapi_delete.as_view(), name="board_delete"),


    # path('board/<int:pk>/delete/', views.delete, name="board_delete"),
    # path('board/create/', views.boardapi_createview, name="board_create"),
    # path('apitest', views.test, name="test"),
    # path('board_write', views.board_write, name="board_write"),
    # path('board_insert', views.board_insert, name="board_insert"),
    # path('board_view', views.board_view, name="board_view"),
    # path('board_update', views.board_update, name="board_update"),
    # path('board_writeajax', views.board_writeajax, name="board_writeajax"),
    # path('board_insertajax', views.board_insertajax, name="board_insertajax"),

    # path('board_ajax', views.board_ajax, name="board_ajax"),
    # path('board_deleteajax', views.board_deleteajax, name="board_deleteajax")
    path('board/comment/create/', views.Commentapi_create.as_view(), name="comment_create"),

    # 로그인 
    path('accounts/login/', views.Login, name="loginview"),
    path('accouts/logout/', views.Logout, name="logoutview"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),

]