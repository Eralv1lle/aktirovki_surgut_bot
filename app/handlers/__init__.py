from .start import start_router
from .actirovka import actirovka_router
from .help import help_router
from .group_events import group_router
from .fallback import fallback_router

routers = [start_router, actirovka_router, help_router, group_router, fallback_router]