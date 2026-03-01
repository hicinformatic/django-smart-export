from typing import Final

from django.utils.version import get_version

default_app_config: str = "django_smart_export.apps.DjangoSmartExportConfig"

VERSION: Final[tuple] = (0, 0, 1, "beta", 0)

__version__: str = get_version(VERSION)

__all__: list[str] = ["__version__"]
