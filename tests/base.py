
from unittest import TestCase


class BaseTestCase(TestCase):
    def setUp(self):
        try:
            import requests_cache
            import datetime

            expire_after = datetime.timedelta(days=3)
            self.session = requests_cache.CachedSession(cache_name='cache', backend='sqlite', expire_after=expire_after)
        except ImportError:
            self.session = None
