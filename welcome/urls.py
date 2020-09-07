from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('contactus/',views.contactus,name='contactus'),
    path('news/',views.news,name='news'),
    path('q-a/',views.qa,name='qa'),
    path('data/',views.data,name='data'),
    path('api/data/',views.get_data,name="api-data"),
    path('',views.HomeView.as_view(),name="chart"),
    path('country/<str:country>/',views.country,name="country"),
    path('api/chart/data',views.ChartData.as_view(),name="api-chart-data"),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))


    ]
