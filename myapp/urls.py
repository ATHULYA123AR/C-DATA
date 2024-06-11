from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("signups",views.signups,name="signups"),
    path("signins", views.signins, name="signins"),
    path("form_success", views.form_success, name="form_success"),
    path("signup_success", views.signup_success, name="signup_success"),
    path("inputs", views.inputs, name="inputs"),
    path("logouts", views.logouts, name="logouts"),

    path("education_view", views.education_view, name="education_view"),
    path("medical_view", views.medical_view, name="medical_view"),
    path("professional_view", views.professional_view, name="professional_view"),
    path("financial_view", views.financial_view, name="financial_view"),
    path("personal_view", views.personal_view, name="personal_view"),
    path('data_view', views.data_view, name='data_view'),

    path('education_update/<int:id1>', views.education_update, name='education_update'),
    path('personal_update/<id2>', views.personal_update, name='personal_update'),
    path('professional_update/<id3>', views.professional_update, name='professional_update'),
    path('financial_update/<id5>', views.financial_update, name='financial_update'),
    path('medical_update/<id4>', views.medical_update, name='medical_update'),

    path('education_delete/<int:id1>', views.education_delete, name='education_delete'),
    path('personal_delete/<id2>', views.personal_delete, name='personal_delete'),
    path('professional_delete/<id3>', views.professional_delete, name='professional_delete'),
    path('financial_delete/<id5>', views.financial_delete, name='financial_delete'),
    path('medical_delete/<id4>', views.medical_delete, name='medical_delete')


    ]
