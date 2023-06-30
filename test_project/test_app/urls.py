from django.urls import re_path
from django.conf.urls import include

from django_url_security.tests import admin


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^grappelli/', include('grappelli.urls'))
]
