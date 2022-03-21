from django.urls import path, include
from .views import RegisterAPI

urlpatterns = [
    # path('user/', admin.site.urls),
      path('dj-rest-auth/', include('dj_rest_auth.urls')),
      path("auth/register/", RegisterAPI.as_view(), name="register"),
    ]