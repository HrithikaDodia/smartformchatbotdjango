from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from channels.sessions import SessionMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from chatbotapp.consumers import ChatConsumer

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        SessionMiddlewareStack(
            URLRouter(
                [
                    url(r"^chat/messages/$", ChatConsumer),
                ]
            )
        )
    )
})