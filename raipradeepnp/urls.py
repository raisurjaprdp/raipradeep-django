from django.contrib import admin
from django.urls import path
from website import views  # or include your app's URLs properly
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
