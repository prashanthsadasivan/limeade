
from handlers.login import HomeHandler, SignUpHandler, LoginHandler
from handlers.video import VideoListHandler
import tornado.web
from settings import settings

url_patterns = [
    (r"/", HomeHandler),
    (r"/v/([a-zA-Z0-9]+)", HomeHandler),
    (r"/videos/$", VideoListHandler),
    (r"/static/*", tornado.web.StaticFileHandler, dict(path= settings['static_path'])),
]
