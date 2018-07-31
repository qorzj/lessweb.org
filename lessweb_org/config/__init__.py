from importlib import import_module
from os import environ
from collections import namedtuple


Config = namedtuple('Config', [
    'db_uri',
    'db_echo',
    'is_test',
])


def get_config() -> Config:
    return import_module('lessweb_org.config.' + environ.get('LESS_ENV', 'local')).config