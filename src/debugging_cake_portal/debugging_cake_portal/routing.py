from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import user_chat.routing


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            user_chat.routing.websocket_urlpatterns
        )
    ),
})
