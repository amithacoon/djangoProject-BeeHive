"""
URL configuration for djangoProject.

This `urlpatterns` list routes URLs to views. For more detailed information, see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views:
    - Add an import:  from my_app import views
    - Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views:
    - Add an import:  from other_app.views import Home
    - Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf:
    - Import the include() function: from django.urls import include, path
    - Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.csv_upload_view),  # Correct usage
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
