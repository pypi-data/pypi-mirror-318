# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['roktools', 'roktools.gnss', 'roktools.orbit', 'roktools.parsers.rtklib']

package_data = \
{'': ['*'], 'roktools': ['c_ext/include/*', 'c_ext/src/*']}

install_requires = \
['numpy>=2.2.1,<3.0.0', 'pandas>=2.2.1,<3.0.0', 'pyarrow>=18.0.0,<19.0.0']

entry_points = \
{'console_scripts': ['cl = roktools.cl:entry_point',
                     'compute_cdf = roktools.stats:cdf_cli',
                     'merge_rinex_nav = roktools.rinex:merge_nav_cli',
                     'rinex_from_file = roktools.rinex:rinex_from_file',
                     'rinex_to_parquet = roktools.rinex:rinex_to_parquet',
                     'tensorial = roktools.tensorial:entry_point']}

setup_kwargs = {
    'name': 'roktools',
    'version': '6.9.0',
    'description': 'Package with utilities and tools for GNSS data processing',
    'long_description': '# pyrok-tools\n\nPython tools used in internal Rokubun projects. This repository contains the following modules:\n\n- `logger`, a module that extends basic Python logging\n- `geodetic`, to perform basic geodetic transformation (Cartesian to Geodetic,\n  Cartesian to Local Tangential Plane, ...)\n\n## Installation\n\nTo make sure that the extensions are installed along with the package, run\n\n`pip install roktools*.whl`\n\n\n## Modules\n\n### Logger\n\nExample of how to use the logger module:\n```python\n>>> from roktools import logger\n>>> logger.set_level("DEBUG")\n>>> logger.debug("Debug message")\n2020-05-05 18:23:55,688 - DEBUG    - Debug message\n>>> logger.warning("Warning message")\n2020-05-05 18:24:11,327 - WARNING  - Warning message\n>>> logger.info("Info message")\n2020-05-05 18:24:26,021 - INFO     - Info message\n>>> logger.error("Error message")\n2020-05-05 18:24:36,090 - ERROR    - Error message\n>>> logger.critical("Critical message")\n2020-05-05 18:24:43,562 - CRITICAL - Critical message\n>>> logger.exception("Exception message", ValueError("Exception message")\n2020-05-05 18:25:11,360 - CRITICAL - Exception message\nValueError: Exception message\nTraceback (most recent call last):\n  File "<stdin>", line 1, in <module>\n  File "/Users/alexlopez/Work/00.General/01.Software/py-roktools/roktools/logger.py", line 46, in exception\n    raise exception\nValueError: Exception message\n```\n\n\n## Deployment to PyPi\n\nThe project is published automatically using internal Gitlab CI on each commit to master to PyPi repository [roktools](https://pypi.org/project/roktools/)\n\nIt uses semantic versioning and conventional commits to set the version and [semantic-release](https://python-semantic-release.readthedocs.io/en/latest/index.html) as\nversioning tool.\n\n\n',
    'author': 'Rokubun',
    'author_email': 'info@rokubun.cat',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}
from scripts.build_extension import *
build(setup_kwargs)

setup(**setup_kwargs)
