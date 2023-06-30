from django.urls import (
    include,
    path,
)

from . import views

app_name = 'test_app'
urlpatterns = [
    path(
        'public/',
        include(
            [
                path('basic', views.basic_public_view, name='basic_public'),
                path(
                    'basic_fixture/<int:pk>',
                    views.basic_public_view_requiring_fixture,
                    name='basic_public_fixture',
                ),
            ],
        ),
    ),
    path(
        'private/',
        include(
            [
                path(
                    'basic_redirects',
                    views.basic_private_view_that_redirects,
                    name='basic_private_redirects',
                ),
                path(
                    'basic_403',
                    views.basic_private_view_that_raises_403,
                    name='basic_private_view_that_raises_403',
                ),
            ],
        ),
    ),
]
