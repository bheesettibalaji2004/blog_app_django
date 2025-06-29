from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register_user, name="register"),
    path("logout/", views.logout_user, name="logout"),
    path("login/", views.login_user, name="login"),
    path("createpost/", views.create_post, name="createpost"),
    path("viewpost/<str:pk>", views.view_post, name="viewpost"),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
