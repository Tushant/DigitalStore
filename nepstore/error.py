from rest_framework.response import Response

# Generic unknown error (most likely to be server error, hence 5xx)
CON_UNKNOWN_ERROR = 500

# Error in User Request (for instance missing id)
CON_BAD_REQUEST = 400

CON_PERMISSION_DENIED = 403

# Object Not Found error
CON_RESOURCE_NOT_FOUND = 404

CON_VALIDATION_ERROR = 100
"""
Errors derived from this class are for those users those who stray from usual behaviour (aka, hackers) or for developers. Hence, mostly, we are not being specific about the error.
"""
class DigitalStoreError(object):
    """
    Base Error class for Connyct
    """
    def __init__(self, code, message, status_code=400):
        """
        code Connyct Error Code
        message Error message
        status_code HTTP REST CODE
        """
        self.error_code = code
        self.error_message = message
        self.status_code = status_code

    def as_response(self, status_code=None):
        if status_code is None:
            status_code = self.status_code

        error = {
            "code": self.error_code,
            "msg": self.error_message,
        }
        return Response({'errors': [error]}, status_code)

"""
Validation errors are more specific and informative. This is derived from
"""
class ValidationError():
    def __init__(self, errors, status_code=400):
        self.status_code = status_code
        self.errors = []
        print('[#]', errors)
        for field, error in errors.items():
            # error is always one of list or dict
            if isinstance(error, list):
                self._add_error(field, error[0])
            elif isinstance(error, dict):
                self._add_error(error)

    def _add_error(self, field, error):
        err = { 'field': field,
                'code': CON_VALIDATION_ERROR, } # Default code

        if isinstance(error, str):
            err['msg'] = error
        elif isinstance(error, dict):
            err['msg'] = error['msg']   # msg is required
            try:
                err['code'] = error['code']     # optional (set default)
            except:
                pass

        self.errors.append(err)

    def as_response(self, status_code=None):
        if status_code is None:
            status_code = self.status_code

        return Response({'errors': self.errors}, status_code)


class UnknownError(DigitalStoreError):
    """
    This is most likely server error. Mostly used in last block of 'except' during response.
    """
    def __init__(self, message="Unknown Error"):
        super(UnknownError, self).__init__(CON_UNKNOWN_ERROR, message, 500)

class PermissionDenied(DigitalStoreError):
    """
    Generic Bad Request
    """
    def __init__(self, message="Permission Denied"):
        super(PermissionDenied, self).__init__(CON_PERMISSION_DENIED, message, 403)


class BadRequest(DigitalStoreError):
    """
    Generic Bad Request
    """
    def __init__(self, message="Bad Request"):
        super(BadRequest, self).__init__(CON_BAD_REQUEST, message, 400)

class RequestedResourceNotFound(DigitalStoreError):
    """
    Generic Resource Not Found
    """
    def __init__(self, message="No such resource"):
        super(RequestedResourceNotFound, self).__init__(CON_RESOURCE_NOT_FOUND, message, 404)
