from typing import Any


class DjangoSmartExportBackend:
    """Base class for export backends."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Initialize the export backend.

        This method can be overridden by subclasses to add custom initialization logic.
        """
        raise NotImplementedError("Subclasses must implement __init__ method.")

    def export(self, data: Any, *args: Any, **kwargs: Any) -> Any:
        """
        Export data in the desired format.

        This method should be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")
