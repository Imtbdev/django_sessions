from django.urls import path
from .views import (
    cookie_session,
    cookie_delete,
    create_session,
    access_session,
    delete_session,
)

urlpatterns = [
    path("testcookie/", cookie_session),
    path("deletecookie/", cookie_delete),
    path("create/", create_session),
    path("access/", access_session),
    path("delete/", delete_session),
]
