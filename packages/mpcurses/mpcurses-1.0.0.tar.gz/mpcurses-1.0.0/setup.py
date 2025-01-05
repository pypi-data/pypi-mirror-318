#!/usr/bin/env python
#   -*- coding: utf-8 -*-

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'mpcurses',
        version = '1.0.0',
        description = 'The mpcurses module facilitates seamless terminal screen updates from child processes within a multiprocessing worker pool, leveraging the curses library for terminal manipulation',
        long_description = '# mpcurses\n[![build+test](https://github.com/soda480/mpcurses/actions/workflows/main.yml/badge.svg)](https://github.com/soda480/mpcurses/actions/workflows/main.yml)\n[![coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](https://pybuilder.io/)\n[![complexity](https://img.shields.io/badge/complexity-A-brightgreen)](https://radon.readthedocs.io/en/latest/api.html#module-radon.complexity)\n[![vulnerabilities](https://img.shields.io/badge/vulnerabilities-None-brightgreen)](https://pypi.org/project/bandit/)\n[![PyPI version](https://badge.fury.io/py/mpcurses.svg)](https://badge.fury.io/py/mpcurses)\n[![python](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-teal)](https://www.python.org/downloads/)\n\nThe mpcurses package facilitates seamless terminal screen updates from child processes within a multiprocessing worker pool - leveraging the curses library for terminal manipulation. The `MPcurses` class is a subclass of [MPmq](https://pypi.org/project/mpmq/); a multiprocessing message queue which enables inter-process communication (IPC) between child workers and a parent process through queuing and consumption of log messages. Mpcurses provides a lightweight abstraction for the curses terminal screen, representing it as a Python dictionary. It includes predefined directives for updating the screen, encompassing:\n\n- Numeric counter management\n- Match messages using regular expressions\n- Text value and color updates\n- Visual indicator maintenance\n- Progress bar rendering\n- Table and list displays\n\n Refer to the MPcurses documentation here: https://soda480.github.io/mpcurses/\n\n### Installation\n```bash\npip install mpcurses\n```\n### Examples\n\nInvoke a single child process to execute a task defined by the `do_something` function. Mpcurses captures all log messages and sends them to a thread-safe queue, the main process consumes messages and uses regular expressions to update the screen which is represented as a dictionary.\n\n```python\nfrom mpcurses import MPcurses\nimport namegenerator, time, logging\nlogger = logging.getLogger(__name__)\n\ndef do_something(*args):\n    for _ in range(0, 400):\n        logger.debug(f\'processing item "{namegenerator.gen()}"\')\n        time.sleep(.01)\n\nMPcurses(\n    function=do_something,\n    screen_layout={\n        \'display_item\': {\n            \'position\': (1, 1), \'text\': \'Processing:\', \'text_color\': 0, \'color\': 14,\n            \'clear\': True, \'regex\': r\'^processing item "(?P<value>.*)"$\'}\n    }).execute()\n ```\n\nExecuting the code above results in the following:\n![example](https://raw.githubusercontent.com/soda480/mpcurses/master/docs/images/demo.gif)\n\n**NOTE** none of the functions being executed in any of the examples include information about the curses screen, multiprocessing or messaging queue - this is handled seamlessly by mpcurses.\n\nBuild the Docker image using the instructions below, run the examples. `python examples/##/sample.py`\n\n#### [Prime Numbers Counter](https://github.com/soda480/mpcurses/blob/master/examples/03/sample.py)\n\nExecute a function that calculates prime numbers for a set range of integers. Execution is scaled across 7 different workers where each process computes the primes for a different range of numbers. For example, the first worker computes primes for the range 1-10K, second worker computes for the range 10K-20K, etc. The main process keeps track of the number of prime numbers encountered for each worker and shows overall progress for each worker using a progress bar.\n\n![example](https://raw.githubusercontent.com/soda480/mpcurses/master/docs/images/example3.gif)\n\n#### [Item Processor](https://github.com/soda480/mpcurses/blob/master/examples/06/sample.py)\n\nExecute a function that processes a list of random items. Execution is scaled across 3 workers where each worker processes a unique set of items. The main process maintains indicators showing the number of items that have been processed by each worker; counting the number of Successful, Errors and Warnings. Three lists are also maintained, one for each group that list which specific items had Warnings and Failures.\n\n![example](https://raw.githubusercontent.com/soda480/mpcurses/master/docs/images/example6.gif)\n\n#### [Bay Enclosure Firmware Update](https://github.com/soda480/mpcurses/blob/master/examples/09/sample.py)\n\nExecute a function that contains a workflow containing tasks to update firmware on a server residing in a blade enclosure. Execution is scaled across a worker pool with five active workers. The main process updates the screen showing status of each worker as they execute the workflow tasks for each blade server. \n\n![example](https://raw.githubusercontent.com/soda480/mpcurses/master/docs/images/example9.gif)\n\n### Projects using `mpcurses`\n\n* [edgexfoundry/sync-github-labels](https://github.com/edgexfoundry/cd-management/tree/git-label-sync) A script that synchronizes GitHub labels and milestones\n\n* [edgexfoundry/prune-github-tags](https://github.com/edgexfoundry/cd-management/tree/prune-github-tags) A script that prunes GitHub pre-release tags\n\n### Development\n\nClone the repository and ensure the latest version of Docker is installed on your development server.\n\nBuild the Docker image:\n```sh\ndocker image build \\\n-t mpcurses:latest .\n```\n\nRun the Docker container:\n```sh\ndocker container run \\\n--rm \\\n-it \\\n-v $PWD:/code \\\nmpcurses:latest \\\nbash\n```\n\nExecute the build:\n```sh\npyb -X\n```\n',
        long_description_content_type = 'text/markdown',
        classifiers = [
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Programming Language :: Python :: 3.12'
        ],
        keywords = '',

        author = 'Emilio Reyes',
        author_email = 'soda480@gmail.com',
        maintainer = '',
        maintainer_email = '',

        license = 'Apache License, Version 2.0',

        url = 'https://github.com/soda480/mpcurses',
        project_urls = {},

        scripts = [],
        packages = ['mpcurses'],
        namespace_packages = [],
        py_modules = [],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = ['mpmq'],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        python_requires = '',
        obsoletes = [],
    )
