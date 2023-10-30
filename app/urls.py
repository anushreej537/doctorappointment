from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('signup/',views.signup),
    path('registration/',views.registration),
    path('login/',views.login),
    path('login_user/',views.login_user),
    path('dashboard/',views.dashboard),
    # path('table/',views.table),
    path('admin_data/',views.admin_data),
    path('patientadd/',views.patientadd),
    path('doctorshow/',views.doctorshow)
]
