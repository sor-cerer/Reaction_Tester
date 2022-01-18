from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path("",views.index, name="index"),
    path("resgister", views.register, name="register" ),
    path("user",views.welcome , name="welcome"),
    path("login",views.login_view, name="login"),
    path("logout",views.logout_view, name="logout"),
    path( "info", views.sighin , name="u-info"  ),
    path("play", views.play, name="play"),

    path("profile", views.profile, name="profile"),

    path("lvl", views.lvl , name="lvl" ),
    
   # path("rguser", views.rguserApi),
   # path("rguser/<int:id>/", views.rguserApi),
   # path("savefile", views.savefile),
] 

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)