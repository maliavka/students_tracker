import time
from students.models import Logger

from students import model_choices as mch


class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        diff = time.time() - start_time

        admin_url = '/admin'
        if request.path.startswith(admin_url):
            Logger.objects.create(
                path=request.path,
                method=mch.METHOD_CHOICES_REVERSED[request.method],
                time_delta=diff,
                # user_id=...

            )

        return response
