from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView
from interventions.views import patient_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('patients/<int:patient_id>/details', patient_details),
    path('api/', include('api.urls', namespace='api')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

urlpatterns += staticfiles_urlpatterns()
