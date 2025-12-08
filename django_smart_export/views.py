from typing import Any

from django.http import HttpRequest, JsonResponse
from django.views import View


class ExportDummyView(View):
    """Dummy view for export functionality testing."""

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> JsonResponse:
        """Handle GET request for export."""
        return JsonResponse({"status": "success", "message": "Export dummy triggered"})
