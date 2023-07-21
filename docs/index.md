# Django URL Security

Django URL Security provides tests to ensure all the private endpoints in your Django project are private.

## Installation

The package is available on PyPI and can be installed using pip.

```
pip install django-url-security
```

It may be necessary to use `pip3`, it will depend on your local environment.

## Quickstart

Run the `export_url_security_file` command.

```
manage.py export_url_security_file
```

This will generate a CSV file in the root directory of your Django project listing all the URL endpoints exposed by your application.

```
status,pattern_name,reference,simplified_regex,is_public,notes
NEW?,landing_page_view,tod_django.views.landing_page_view,/,private,
NEW?,login_view,tod_django.views.login_view,/login/,private,
NEW?,subjects_view,tod_django.views.subjects_view,/subjects/,private,
NEW?,quiz_view_stub,tod_django.views.quiz_view,/subjects/<path:object_id>/quiz/,private,
```

Now run the tests for the project to confirm the URL security tests are in place. Alternatively run _only_ the URL security tests by passing `django_url_security.url_security` to the `test` command.

```
# run all tests, include the newly added url security tests
manage.py test

# run only the url security tests
manage.py test django_url_security.url_security
```

Under the current configuration, the tests should pass because the `status` for each endpoint is set to `NEW?`. This is a placeholder value used to indicate that the endpoint has recently been added the URL security specification. This value should be updated so that the tests make the correct assertions about the expected behaviour of each endpoint.

```
status,pattern_name,reference,simplified_regex,is_public,notes
OK,landing_page_view,tod_django.views.landing_page_view,/,PUBLIC,
OK,login_view,tod_django.views.login_view,/login/,PUBLIC,
OK,subjects_view,tod_django.views.subjects_view,/subjects/,private,
FAILING,quiz_view_stub,tod_django.views.quiz_view,/subjects/<path:object_id>/quiz/,private,Not yet implemented
```

In this case, our URL security tests will only pass if:

- `tod_django.views.landing_page_view` and `tod_django.views.login_view` are publicly accessible and returns `200 OK` in response to HTTP `GET` requests.
- `tod_django.views.subjects_view` is only accessible to authenticated users and returns `200 OK` in response to HTTP `GET` requests from authenticated users.
- `tod_django.views.quiz_view` is only accessible to authenticated users and returns a failure status in response to HTTP `GET` requests from authenticated users. Note that the `notes` field can be used to annotate endpoints with additional information which is useful when, for example, documenting expected failures.

If each endpoint conforms to the behaviour described above, the tests for the project should now pass.
