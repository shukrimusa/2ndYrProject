from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, ContentPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),

    path('about/', AboutPageView.as_view(), name='about'),

    path('contact us/', ContactPageView.as_view(), name='contact'),
    path('content/', ContentPageView.as_view(), name='content'),

]
