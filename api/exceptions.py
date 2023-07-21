from rest_framework import exceptions, status


class ObjectAlreadyExists(exceptions.APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'Object already exists'
    default_code = 'already_exists'