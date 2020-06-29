# Reference:
# https://werkzeug.palletsprojects.com/en/1.0.x/wsgi/#iterator-stream-helpers
# https://github.com/pallets/werkzeug/blob/master/src/werkzeug/middleware/profiler.py


from werkzeug.wrappers import Request
from werkzeug.wsgi import ClosingIterator


class TrackingMiddleware():
    def __init__(self, app, log_callback):
        self.app = app
        self.log_callback = log_callback

    def __call__(self, environ, start_response):
        body = list(self.app(environ, start_response))


        def _log():
            self.log_callback(Request(environ), body)


        return ClosingIterator(body, _log)


def configure_app(app, log_callback):
    app.wsgi_app = TrackingMiddleware(app.wsgi_app, log_callback)
