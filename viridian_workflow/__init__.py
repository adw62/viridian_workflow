from pkg_resources import get_distribution

try:
    __version__ = get_distribution("viridian_workflow").version
except:
    __version__ = "local"

__all__ = [
    "amplicon_schemes",
    "config",
    "detect_primers",
    "minimap",
    "one_sample_pipeline",
    "primers",
    "qcovid",
    "sample_reads",
    "tasks",
    "utils",
]

from viridian_workflow import *
