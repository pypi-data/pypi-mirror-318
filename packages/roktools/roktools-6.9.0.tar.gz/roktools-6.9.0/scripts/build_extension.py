from distutils.errors import CCompilerError, DistutilsExecError, DistutilsPlatformError
from typing import Dict, Any

from setuptools import Extension
from setuptools.command.build_ext import build_ext

import numpy as np

ext_modules = [
        Extension(
        "roktools.c_ext",
        sources=["roktools/c_ext/src/foo.c", "roktools/c_ext/src/helpers.c", "roktools/c_ext/src/hatanaka.c", "roktools/c_ext/src/mtable_init.c",
                 "submodules/hatanakalib/hatanaka/src/common.c", "submodules/hatanakalib/hatanaka/src/crx2rnx.c"],
        include_dirs=["roktools/", "submodules/hatanakalib", np.get_include()]
    )
]

class BuildFailed(Exception):
    pass


class ExtBuilder(build_ext):
    def run(self):
        try:
            build_ext.run(self)
        except (DistutilsPlatformError, FileNotFoundError):
            pass

    def build_extension(self, ext):
        try:
            build_ext.build_extension(self, ext)
        except (CCompilerError, DistutilsExecError, DistutilsPlatformError, ValueError):
            pass


def build(setup_kwargs: Dict[str, Any]) -> None:
    setup_kwargs.update(
        {
            "ext_modules": ext_modules,
            "zip_safe": False,
            "cmdclass": {"build_ext": ExtBuilder}
        }
    )
