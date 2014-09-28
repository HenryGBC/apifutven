from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from equipos.views import EquipoViewSet
from fechas.views import FechaViewSet
from resumen_fecha.views import ResumenViewSet
from tabla.views import TablaViewSet

router = DefaultRouter()
router.register(r'equipos', EquipoViewSet)
router.register(r'fechas', FechaViewSet)
router.register(r'resumenes', ResumenViewSet)
router.register(r'tabla', TablaViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'apifutven.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
