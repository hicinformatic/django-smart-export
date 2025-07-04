from django.http import JsonResponse
from django.views import View

class ExportDummyView(View):
    def get(self, request):
        # Ici tu ajouteras ta logique export dynamique, formats, config, etc.
        return JsonResponse({"status": "success", "message": "Export dummy triggered"})
