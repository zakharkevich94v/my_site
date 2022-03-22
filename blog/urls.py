from django.urls import path
from .views import (
    HomeView, 
    WorksPageView, 
    WorksByCategoryView, 
    GetWorkView,
    contact_me
)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('works/', WorksPageView.as_view(), name='works'),
    path('about/<str:slug>/', GetWorkView.as_view(), name='about-work'),
    path('works/<str:slug>/', WorksByCategoryView.as_view(), name='works-by-category'), 
    path('contact/', contact_me, name='contact-me'),   
]



handler404 = "blog.views.page_not_found_view"