from django.urls import path

from rest_api.views import PageList, PageDetail

urlpatterns = [
    path("", PageList.as_view(), name="Page_list"),
    path("<int:pk>/", PageDetail.as_view(), name="Page_detail")
]
