from django.urls import path
from . import views
urlpatterns = [path('', views.homepage, name='homepage'),
                path('login/', views.login, name='login'),
                path('reportcrime/', views.reportcrime, name='reportcrime'),
                path('showreports/', views.showreports, name='showreports'),
                path('reportadded/', views.reportadded, name='reportadded'),
                path("reportcrime/submit/", views.reportcrime_db, name="reportcrime_db"),
                path('about/', views.about, name='about'),
                ]