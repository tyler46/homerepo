import os
# Normally you should not import ANYTHING from Django directly
# into our settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    """Gets the environment variable or returns exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s enviroment variable" % var_name
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_env_variable('HOMEREPO_SECRET_KEY')
