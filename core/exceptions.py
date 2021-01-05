
class BusinessException(Exception):
    def __init__(self, code=None, msg=None, func=None, url=None):
        self.code = code
        self.msg = msg
        self.func = func
        self.url = url

class PermissionDenied(Exception):
    """The user did not have permission to do that"""
    pass


class ViewDoesNotExist(Exception):
    """The requested view does not exist"""
    pass


class MiddlewareNotUsed(Exception):
    """This middleware is not used in this server configuration"""
    pass


class ImproperlyConfigured(Exception):
    """Django is somehow improperly configured"""
    pass


class FieldError(Exception):
    """Some kind of problem with a model field."""
    pass