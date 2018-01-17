
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # matches myfile/
    path('myfile/', include('myfiles.urls')),

]
