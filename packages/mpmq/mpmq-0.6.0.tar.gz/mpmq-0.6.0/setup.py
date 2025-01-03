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
        name = 'mpmq',
        version = '0.6.0',
        description = 'The mpmq module enables seamless interprocess communication between a parent and child processes when parallelizing a task across multiple workers.',
        long_description = '# mpmq\n[![GitHub Workflow Status](https://github.com/soda480/mpmq/workflows/build/badge.svg)](https://github.com/soda480/mpmq/actions)\n[![vulnerabilities](https://img.shields.io/badge/vulnerabilities-None-brightgreen)](https://pypi.org/project/bandit/)\n[![coverage](https://img.shields.io/badge/coverage-99%25-brightgreen)](https://pybuilder.io/)\n[![complexity](https://img.shields.io/badge/complexity-A-brightgreen)](https://radon.readthedocs.io/en/latest/api.html#module-radon.complexity)\n[![PyPI version](https://badge.fury.io/py/mpmq.svg)](https://badge.fury.io/py/mpmq)\n[![python](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-teal)](https://www.python.org/downloads/)\n\nThe mpmq module enables seamless interprocess communication between a parent and child processes when parallelizing a task across multiple workers. The `MPmq` class defines a custom log handler that sends all log messages from child workers to a thread-safe queue that the parent can consume and handle. This is helpful in cases where you want the parent to show real-time progress of child workers as they execute a task.\n\n### Installation\n```bash\npip install mpmq\n```\n\n### `MPmq class`\n```\nmpmq.MPmq(function, process_data=None, shared_data=None, processes_to_start=None)\n```\n> `function` - the function represents the task you wish the child workers to execute\n\n> `process_data` - list of dictionaries where each dictionary contains the arguments that will be sent to each background child process executing the function; the length of the list dictates the total number of processes that will be executed\n\n> `shared_data` - a dictionary containing arbitrary data that will be sent to all processes as key word arguments\n\n> `process_to_start` - the number of processes to initially start; this represents the number of concurrent processes that will be running. If the total number of processes is greater than this \nnumber then execution will be queued and executed to ensure that this concurrency is maintained\n\n> **execute(raise_if_error=False)**\n>> Start execution the process’s activity. If `raise_if_error` is set to True, an exception will be raised if any function encountered an error during execution.\n\n> **process_message(offset, message)**\n>> Process a message sent from one of the background workers executing the function. The `offset` represents the index of the executing Process; this number is the same as the corresponding index within the `process_data` list that was sent to the constructor. The `message` represents the message that was logged by the function. \n\n### Examples\n\n The primary intent is for the MPmq class to be used as a superclass where the subclass ovverrides the `process_message` method to handle messages coming in from the child workers. The following example demonstrate how this can be done.\n\n#### [Worker Status as a Progress Bar](https://github.com/soda480/mpmq/blob/main/examples/example1.py)\n\nThe example parallizezes a task across multiple processes using a pool of worker processes. Status of each worker is shown as a Progress Bar, as each Child worker in the pool completes an item defined in the task the Parent updates a Progress Bar.\n\n![example](https://raw.githubusercontent.com/soda480/mpmq/main/docs/images/example1.gif)\n\n\n#### [Worker Status as a List](https://github.com/soda480/mpmq/blob/main/examples/example2.py)\n\nThe example parallizezes a task across multiple processes using a pool of worker processes. Status of each worker is shown using an array where each index of the array represents an individual worker, as each Child worker in the pool completes the associated item in the List is updated with the completed message.\n\n![example](https://raw.githubusercontent.com/soda480/mpmq/main/docs/images/example2.gif)\n\n\n### Projects using `mpmq`\n\n* [`mpcurses`](https://pypi.org/project/mpcurses/) An abstraction of the Python curses and multiprocessing libraries providing function execution and runtime visualization capabilities\n\n* [`mppbars`](https://pypi.org/project/mppbar/) Scale execution of a function across multiple across a number of background processes while displaying their execution status via a progress bar\n\n* [`mp4ansi`](https://pypi.org/project/mp4ansi/) A simple ANSI-based terminal emulator that provides multi-processing capabilities\n\n### Development\n\nClone the repository and ensure the latest version of Docker is installed on your development server.\n\nBuild the Docker image:\n```sh\ndocker image build \\\n-t mpmq:latest .\n```\n\nRun the Docker container:\n```sh\ndocker container run \\\n--rm \\\n-it \\\n-v $PWD:/code \\\nmpmq:latest \\\nbash\n```\n\nExecute the build:\n```sh\npyb -X\n```\n',
        long_description_content_type = 'text/markdown',
        classifiers = [
            'Programming Language :: Python',
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

        url = 'https://github.com/soda480/mpmq',
        project_urls = {},

        scripts = [],
        packages = ['mpmq'],
        namespace_packages = [],
        py_modules = [],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = [],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        python_requires = '',
        obsoletes = [],
    )
