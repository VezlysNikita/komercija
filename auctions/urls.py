from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("view_page/<str:listing_id>", views.view_page, name="view_page"),
    path("addwatchlist/<int:listing_id>", views.addwatchlist, name="addwatchlist"),
    path("watchlist", views.watchlist, name="watchlist"),
]
