__version__ = "1.0.0"

import os

from .cli import start_session
start_session(os.getpid())
