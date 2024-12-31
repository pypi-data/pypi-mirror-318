"""
Python module for **nmk-doc** plugin code.
"""

from importlib.metadata import version

from nmk_base.version import VersionResolver

__title__ = "nmk-doc"
try:
    __version__ = version(__title__)
except Exception:  # pragma: no cover
    __version__ = "unknown"


class NmkDocVersionResolver(VersionResolver):
    """
    Version resolver for **${nmkDocPluginVersion}**
    """

    def get_version(self) -> str:
        """
        Module version accessor

        :return: current module version
        """

        return __version__
