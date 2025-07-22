from django.urls import path
from website.views import index_view,Contact_view,About_view

urlpatterns = [
    path('',index_view),
    path('Contact page', Contact_view),
    path('About page', About_view)
]
