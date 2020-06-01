from . import views
from django.urls import path


urlpatterns=[
            path('', views.project, name='project-list'),
            path('mitm',views.mitmdoit,name='mitm'),
]
