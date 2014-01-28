"""The asyncio package, tracking PEP 3156."""

import sys

# The selectors module is in the stdlib in Python 3.4 but not in 3.3.
# Do this first, so the other submodules can use "from . import selectors".
# Prefer asyncio/selectors.py over the stdlib one, as ours may be newer.
try:
    from . import selectors
except ImportError:
    import selectors  # Will also be exported.

if sys.platform == 'win32':
    # Similar thing for _overlapped.
    try:
        from . import _overlapped
    except ImportError:
        import _overlapped  # Will also be exported.

# This relies on each of the submodules having an __all__ variable.
from .events import *
from .futures import *
from .locks import *
from .protocols import *
from .queues import *
from .streams import *
from .subprocess_streams import *
from .tasks import *
from .transports import *

if sys.platform == 'win32':  # pragma: no cover
    from .windows_events import *
else:
    from .unix_events import *  # pragma: no cover


__all__ = (events.__all__ +
           futures.__all__ +
           locks.__all__ +
           protocols.__all__ +
           queues.__all__ +
           streams.__all__ +
           subprocess_streams.__all__ +
           tasks.__all__ +
           transports.__all__)
