# Copyright 2018 The RLgraph authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import os
from setuptools import setup, find_packages

# Read __version__ avoiding imports that might be in install_requires
version_vars = dict()
with open(os.path.join(os.path.dirname(__file__), 'rlgraph_plot', 'version.py')) as fp:
    exec(fp.read(), version_vars)

install_requires = [
    'rlgraph',
    'flask'
]

setup_requires = []

extras_require = {
}

entry_points = {
    'console_scripts': [
        'rlgraph-plot = rlgraph_plot.__main__:main'
    ]
}

setup(
    name='rlgraph-plot',
    version=version_vars['__version__'],
    description='RLgraph metagraph plotting library',
    url='https://rlcore.ai',
    author='RLcore',
    author_email='dev@rlcore.ai',
    license='Apache 2.0',
    packages=[package for package in find_packages() if package.startswith('rlgraph_plot')],
    install_requires=install_requires,
    setup_requires=setup_requires,
    extras_require=extras_require,
    entry_points=entry_points,
    zip_safe=False
)
