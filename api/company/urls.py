from django.urls import path
from api.company.views import CompanyCreateView

urlpatterns = [
    path('companies/', CompanyCreateView.as_view(), name='company-create')
    # path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    
]