import logging

import keycloak.exceptions
from django.contrib.auth.models import Permission
from requests.exceptions import HTTPError

import django_keycloak.services.client

logger = logging.getLogger(__name__)


def synchronize(client):
    """
    :param django_keycloak.models.Client client:
    :return:
    """
    keycloak_client_id = django_keycloak.services.client.get_keycloak_id(
        client=client)

    role_api = client.admin_api_client.realms.by_name(client.realm.name)\
        .clients.by_id(keycloak_client_id).roles

    for permission in Permission.objects.all():

        try:
            role_api.create(name=permission.codename,
                            description=permission.name)
        except (HTTPError, keycloak.exceptions.KeycloakClientError) as e:
            if isinstance(e, keycloak.exceptions.KeycloakClientError):
                e = e.original_exc
            if e.response.status_code != 409:
                raise

        else:
            continue

        # Update role
        role_api.by_name(permission.codename) \
            .update(name=permission.codename, description=permission.name)
