"""Graceful shutdown management for long-running pipeline operations."""

import logging
import signal

log = logging.getLogger("dc_energy")

_shutdown = False


def is_shutdown() -> bool:
    """Return True if a shutdown has been requested."""
    return _shutdown


def request_shutdown() -> None:
    """Request a graceful shutdown."""
    global _shutdown
    _shutdown = True


def install_signal_handlers() -> None:
    """Install SIGINT/SIGTERM handlers that set the shutdown flag."""
    def _handler(signum, frame):
        request_shutdown()
        log.warning("Shutdown requested — finishing current batch …")

    signal.signal(signal.SIGINT, _handler)
    signal.signal(signal.SIGTERM, _handler)
