
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Student API EndPoints ')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('appone.apiroutes')),
    url(r'^rapi/', include('rest_framework.urls')),
    url(r'^$', schema_view)
]
