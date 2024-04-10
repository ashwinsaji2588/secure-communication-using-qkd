from django.urls import path
from .views import registerview, loginview, logoutview, chat, reviews, decrypt

app_name = 'accounts'

urlpatterns = [
    path('register/', registerview, name="register"),
    path('login/', loginview, name="login"),
    path('logout/', logoutview, name="logout"),
    path('<s_idx>/<r_idx>/chat/', chat, name="chat"),
    path('<id>/<idx>/<add>/reviews/', reviews, name="reviews"),
    path('<id>/<idx>/<info>/<r_idx>/decrypt/', decrypt, name="decrypt"),
]
