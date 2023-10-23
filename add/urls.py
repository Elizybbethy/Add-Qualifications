from add import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('education/', views.EducationView.as_view(), name='education'),
    path('<int:pk>', views.QualificationView.as_view(), name='qualification'),   
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('education/edit/<int:pk>/', views.EditEducationView.as_view(), name='edit_qualification'),
    path('document/', views.DocumentView.as_view(), name='document'),
    path('document/int:pk', views.DocumentDetailsView.as_view(), name='documents'),
]
