from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView
from interventions.views import patient_details, out_patient
from message.views import user_inbox, user_outbox

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('patients/<int:patient_id>/details', patient_details),
    path('api/', include('api.urls', namespace='api')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('inbox/', user_inbox),
    path('outbox/', user_outbox),
    path('patients/<int:patient_id>/out', out_patient),
]

urlpatterns += staticfiles_urlpatterns()
