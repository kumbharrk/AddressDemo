from rest_framework.routers import SimpleRouter
from appone.views import StudentOps,AddressOps
app_routes = SimpleRouter()
app_routes.register('student',StudentOps)
app_routes.register('address',AddressOps)
urlpatterns = app_routes.urls
