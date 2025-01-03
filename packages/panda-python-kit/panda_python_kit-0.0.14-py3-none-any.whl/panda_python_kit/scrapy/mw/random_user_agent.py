from fake_useragent import UserAgent


class UserAgentRandomMiddleware:
    def process_request(self, request, spider):
        ua = UserAgent()
        request.headers['User-Agent'] = ua.random


class UserAgentChromeRandomMiddleware:
    def process_request(self, request, spider):
        ua = UserAgent(browsers=['chrome'])
        request.headers['User-Agent'] = ua.random


class UserAgentHighMiddleware:
    def process_request(self, request, spider):
        ua = UserAgent(min_percentage=3.0)
        request.headers['User-Agent'] = ua.random


class UserAgentCustomMiddleware:

    def __init__(self, min_percentage=3):
        self.min_percentage = min_percentage
        self.ua = UserAgent(min_percentage=self.min_percentage)

    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler.settings["USER_AGENT_MIN_PERCENTAGE"])
        return o

    def process_request(self, request, spider):
        request.headers.setdefault(b"User-Agent", self.ua.random)