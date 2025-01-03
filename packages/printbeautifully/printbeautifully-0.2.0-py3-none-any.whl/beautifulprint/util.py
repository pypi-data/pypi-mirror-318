class ContextManager:
    """
    Class that does nothing but supports context management (with statements)
    """
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return
