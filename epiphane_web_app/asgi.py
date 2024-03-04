"""
ASGI config for epiphane_web_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os, sys
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from dotenv import load_dotenv
from django.core.asgi import get_asgi_application
from chat import routing
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
                
load_dotenv()

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "epiphane_web_app.settings",
)

# from decouple import config
# config("DJANGO_SETTINGS_MODULE", default="epiphane_web_app.settings", cast=str)
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns))
        ),
    }
)