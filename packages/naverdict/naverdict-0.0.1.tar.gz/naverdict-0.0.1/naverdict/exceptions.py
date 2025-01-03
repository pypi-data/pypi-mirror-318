from naverdict.constants import CONNECTION_ERROR_MESSAGE


class NaverDictConnectionError(Exception):
    """
    Exception raised when network is unconnected
    """

    def __init__(self):
        pass

    def __str__(self):
        return CONNECTION_ERROR_MESSAGE

    def __repr__(self):
        return CONNECTION_ERROR_MESSAGE
