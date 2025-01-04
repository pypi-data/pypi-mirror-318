class MonitoroAPIError(Exception):
    """Base exception for Monitoro API errors."""

    pass


class BadRequestError(MonitoroAPIError):
    """Exception for 400 Bad Request errors."""

    pass


class MonitorNotFoundError(MonitoroAPIError):
    """Exception for 404 Monitor Not Found errors."""

    pass


class ServerError(MonitoroAPIError):
    """Exception for 500 Server Error during data extraction."""

    pass
