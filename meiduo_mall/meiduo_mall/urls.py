from django.conf.urls import url, include


urlpatterns = [
    # users
    url(r'^', include('users.urls',)),
]