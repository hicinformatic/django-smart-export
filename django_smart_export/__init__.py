from django.utils.version import get_version

default_app_config = "django_smart_export.apps.DjangoSmartExportConfig"


VERSION = (0, 0, 1, "beta", 0)

__version__ = get_version(VERSION)
