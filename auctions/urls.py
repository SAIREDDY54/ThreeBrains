from django.urls import path

from . import views

from django.conf.urls import url

app_name = "auctions"

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("cards", views.cards_view, name="cards"),
    path("add", views.add, name="add"),
    path("qr", views.qrcode, name="qr"),
    path("otp", views.validateOTP, name="otp"),
    path('chart', views.chartData, name="chart"),
    path("register", views.register, name="register"),
    # path('api', views.ChartData.as_view()),
    path("add_comment", views.add_comment, name="add_comment"),
    path("listing_details", views.listing_details_view, name="listing_details"),
    path("watchlist", views.watchlist_view, name="watchlist"),
    path("category_list", views.category_list, name="category_list"),
    path("category_list/<str:category>", views.category_list_redirect, name="category_list_redirect"),
    path("add_to_watchlist", views.add_to_watchlist, name="add_to_watchlist"),
    path("place_bid", views.place_bid, name="place_bid"),
    path("end_listing", views.end_listing, name="end_listing"),
    path("auctions_history", views.auctions_history, name="auctions_history"),
    path("delete_item_watchlist", views.delete_item_watchlist, name="delete_item_watchlist"),
    path("payment", views.payment, name="payment"),
]
