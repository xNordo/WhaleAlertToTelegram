class BadRequest(Exception):
    """400	Bad Request -- Your request was not valid."""
    pass


class Unauthorized(Exception):
    """401	Unauthorized -- No valid API key was provided"""
    pass


class Forbidden(Exception):
    """403	Forbidden -- Access to this resource is restricted for the given caller."""
    pass


class NotFound(Exception):
    """404	Not Found -- The requested resource does not exist."""
    pass


class MethodNotAllowed(Exception):
    """405	Method Not Allowed -- An invalid method was used to access a resource."""
    pass


class NotAcceptable(Exception):
    """406	Not Acceptable -- An unsupported format was requested."""
    pass


class TooManyRequests(Exception):
    """429	Too Many Requests -- You have exceeded the allowed number of calls per minute. Lower call frequency or upgrade your plan for a higher rate limit."""
    pass


class InternalServerError(Exception):
    """500	Internal Server Error -- There was a problem with the API host server. Try again later."""
    pass


class ServiceUnavilable(Exception):
    """503	Service Unavailable -- API is temporarily offline for maintenance. Try again later."""
    pass
