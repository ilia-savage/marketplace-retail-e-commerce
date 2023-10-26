from django.utils import timezone
from .services import VisitCacheService, should_ignore_url

class VisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not should_ignore_url(request.path_info):
            service = VisitCacheService(request)
            service.add_to_cache()
        response = self.get_response(request)
        return response
    