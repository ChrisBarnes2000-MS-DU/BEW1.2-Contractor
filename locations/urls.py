from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from locations.views import PageListView, PageCreateView, PageDetailView, PageEditView, PageDeleteView

urlpatterns = [
    # ex: /locations
    path('', PageListView.as_view(), name='list-page'),
    # ex: /locations/new/
    path('new/', PageCreateView.as_view(), name='create-page'),
    # ex: /locations/san-francisco/
    path('<str:slug>/', PageDetailView.as_view(), name='details-page'),
    # ex: /locations/edit/
    path('<str:slug>/edit/', PageEditView.as_view(), name='edit-page'),
    # ex: /locations/delete/
    path('<str:slug>/delete/', PageDeleteView.as_view(), name='delete-page'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
