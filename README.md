Django Keycloak
===============

Django app to add Keycloak support to your project.

This fork fixes some bugs and allows you to use KeyCloak to login to the Django admin panel.

Prerequisites
===========
You must create a KeyCloak client, enable "Service Account" setting, set access type to "Confidential", 
set correct login redirect URL and generate client secret.

Client must have the following roles:
1. ```manage-accounts```
2. ```view-profile```


Installation
===========
1. Add package to the project
    
    ```poetry add git+https://github.com/Cactiw/django-keycloak.git#tk-keycloak```
2. Add application to Django INSTALLED_APPS, MIDDLEWARE, AUTHENTICATION_BACKENDS in ```settings.py```
    ```python3
    INSTALLED_APPS = [
        ...
        "django_keycloak.apps.KeycloakAppConfig"
    ]
   
   MIDDLEWARE = [
         ...
        "django_keycloak.middleware.BaseKeycloakMiddleware",
    ]
    AUTHENTICATION_BACKENDS = [
        # Must be presented to keep ability to login through standard Django account.
        "django.contrib.auth.backends.ModelBackend",
        
        # Keycloak backend
        "django_keycloak.auth.backends.KeycloakAuthorizationCodeBackend",
    ]
   ```
3. Add following parameters to ```settings.py```:
   ```python3
   KEYCLOAK_OIDC_PROFILE_MODEL = 'django_keycloak.OpenIdConnectProfile'
   LOGIN_REDIRECT_URL = "/admin"
   LOGOUT_REDIRECT_URL = "/admin"

   # Role name that grants admin access.
   # Users that have this role will have access to admin page.
   KEYCLOAK_ADMIN_ROLE_NAME = "sender-admin"
   
   # Specify KeyCloak client name.
   # It is required to get permissions for Users for this client.
   KEYCLOAK_API_CLIENT_NAME = "django-test"
   ```
4. Add following urls to ```urls.py```: 
   ```python3
   import django_keycloak.views
   
   urlpatterns = [
       # Redirect to KeyKloak login and logout pages.\
       # Place this lines above admin urls definitions for correct override.
       re_path(r'^admin/login/$', django_keycloak.views.AdminLoginKeycloak.as_view(), name='login'),
       re_path(r'^admin/logout/$', django_keycloak.views.admin_keycloak_logout, name='logout'),
   
       path("admin/", admin.site.urls),
       re_path(r'^keycloak/', include('django_keycloak.urls')),
   ]
   ```
5. Make django-keycloak migrations: ```python manage.py migrate django_keycloak```.
You can roll back these migrations with ```python manage.py migrate django_keycloak zero```
6. Login through root Django account to admin page.
7. Add KeyCloak server and Realm.
8. For created Realm perform "Refresh OpenID Connect .well-known" action.
9. For created Realm perform "Synchronize permissions" action. 
KeyCloak client must have "manage-users" permission to do this! 
This action can take several minutes depending on your Django models count.
10. You can read more about steps 6-8 in the documentation: https://django-keycloak.readthedocs.io/en/latest/scenario/initial_setup.html

