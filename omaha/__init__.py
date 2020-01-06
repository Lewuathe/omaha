import logging

from .client import Client
from .indicator import Indicator
from .version import __version__

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)

__all__ = ["__version__", "Client", "DataFrame"]
