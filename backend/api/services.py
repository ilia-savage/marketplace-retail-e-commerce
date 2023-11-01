import json
from django.core.cache import cache
from django.utils import timezone
from .models import Visit
from user.models import User
from user.auth import get_user

import redis


def should_ignore_url(url):
    # no /admin or /auth
    return url.startswith('/admin/') or url.startswith('/auth/')

class VisitCacheService:
    def __init__(self, request):
        self.request = request

    def _prepare_visit_data(self):
        date = timezone.now()
        formatted_date = date.strftime("%Y-%m-%d %H:%M:%S")
        try:
            user = get_user(self.request)["username"]

        except:
            user = None
        data = {
            "user": user,
            "date": formatted_date,
            "url": self.request.path,
            "ip": self.request.META.get("REMOTE_ADDR"),
            "browser": self.request.META.get("HTTP_USER_AGENT"),
        }
        return data

    def _get_key_name(self):
        # unique key
        date = timezone.now()
        formatted_date = date.strftime("%Y-%m-%d %H:%M:%S")
        user_ip = self.request.META.get("REMOTE_ADDR")
        key = f"visit:{user_ip}:{formatted_date}"
        key = key.replace(" ", "__")
        
        return key

    def add_to_cache(self):
        data = self._prepare_visit_data()
        key = self._get_key_name()
        cache.set(key, json.dumps(data))

class VisitDataBaseService:
    def save_to_db(self):
        
        redis_client = redis.StrictRedis(host='redis', port=6379, db=0)
        keys = redis_client.keys(':1:visit:*')

        for key in keys:
            key_decoded = key.decode("utf-8")
            key_formatted = key_decoded.replace(":1:", "")
            data_json = cache.get(key_formatted)
            print(data_json)
            # User.objects.get(username=data["user"])
            if data_json:
                data = json.loads(data_json)
                try:
                    user = User.objects.get(username=data["user"])
                    
                except:
                    user = None
                visit = Visit(
                    user=user,
                    date=data["date"],
                    url=data["url"],
                    ip=data["ip"],
                    browser=data["browser"],
                )
                visit.save()
                cache.delete(key_formatted)