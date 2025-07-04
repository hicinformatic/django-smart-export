class DjangoSmartExportBackend:
    """
    Base class for export backends.
    All export backends should inherit from this class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the export backend.
        This method can be overridden by subclasses to add custom initialization logic.
        """
        raise NotImplementedError("Subclasses must implement __init__ method.")

    def export(self, data, *args, **kwargs):
        """
        Export data in the desired format.
        This method should be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")
