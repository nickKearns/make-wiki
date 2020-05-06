from django.urls import path, include
from wiki.views import PageListView, PageDetailView, PageCreateView
from accounts.views import SignupView


urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('newpage', PageCreateView.as_view(), name='create')


]
