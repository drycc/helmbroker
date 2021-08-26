import os

HELMBROKER_ROOT = os.environ.get("HELMBROKER_CELERY_BROKER", '/etc/helmbroker')

ADDONS_PATH = os.path.join(HELMBROKER_ROOT, 'addons')
CONFIG_PATH = os.path.join(HELMBROKER_ROOT, 'config')
INSTANCES_PATH = os.path.join(HELMBROKER_ROOT, 'instances')

USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')


class Config:
    DEBUG = os.environ.get("DEBUG", False)
