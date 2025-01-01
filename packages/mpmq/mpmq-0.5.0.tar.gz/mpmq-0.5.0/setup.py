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
        version = '0.5.0',
        description = 'Mpmq is an abstraction of the Python multiprocessing library providing execution pooling and message queuing capabilities.',
        long_description = '# mpmq\n[![GitHub Workflow Status](https://github.com/soda480/mpmq/workflows/build/badge.svg)](https://github.com/soda480/mpmq/actions)\n[![vulnerabilities](https://img.shields.io/badge/vulnerabilities-None-brightgreen)](https://pypi.org/project/bandit/)\n[![coverage](https://img.shields.io/badge/coverage-99%25-brightgreen)](https://pybuilder.io/)\n[![complexity](https://img.shields.io/badge/complexity-A-brightgreen)](https://radon.readthedocs.io/en/latest/api.html#module-radon.complexity)\n[![PyPI version](https://badge.fury.io/py/mpmq.svg)](https://badge.fury.io/py/mpmq)\n[![python](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-teal)](https://www.python.org/downloads/)\n\nThe mpmq module provides a convenient way to scale execution of a function across multiple input values by distributing the input across a specified number of background processes. It also provides the means for the caller to intercept and process messages from the background processes while they execute the function. It does this by configuring a custom log handler that sends the function\'s log messages to a thread-safe queue; several API\'s are provided for the caller to process the messages from the message queue. The number of processes along with the input data for each process is specified as a list of dictionaries. The number of elements in the list dictates the total number of processes to execute. The result of each function is returned as a list to the caller after all background workers complete.\n\nThe main features are:\n\n* execute function across multiple processes\n* queue function execution\n* create log handler that sends function log messages to thread-safe message queue\n* process messages from log message queue\n* maintain result of all executed functions\n* terminate execution using keyboard interrupt\n\n### Installation\n```bash\npip install mpmq\n```\n\n### `MPmq class`\n```\nmpmq.MPmq(function, process_data=None, shared_data=None, processes_to_start=None)\n```\n> `function` - the function to execute\n\n> `process_data` - list of dictionaries where each dictionary contains the key word arguments that will be sent to each background process executing the function; the length of the list dictates the total number of processes that will be executed\n\n> `shared_data` - a dictionary containing arbitrary data that will be sent to all processes as key word arguments\n\n> `process_to_start` - the number of processes to initially start; this represents the number of concurrent processes that will be running. If the total number of processes is greater than this \nnumber then execution will be queued and executed to ensure that this concurrency is maintained\n\n> **execute(raise_if_error=False)**\n>> Start execution the process’s activity. If `raise_if_error` is set to True, an exception will be raised if any function encountered an error during execution.\n\n> **process_message(offset, message)**\n>> Process a message sent from one of the background processes executing the function. The `offset` represents the index of the executing Process; this number is the same as the corresponding index within the `process_data` list that was sent to the constructor. The `message` represents the message that was logged by the function.\n\n### Examples\n\nA simple example using mpmq:\n\n```python\nfrom mpmq import MPmq\nimport sys, logging\nlogger = logging.getLogger(__name__)\nlogging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(processName)s [%(funcName)s] %(levelname)s %(message)s")\n\ndef do_work(pid=None, number=None):\n    logger.info(f"hello from process: {pid}")\n    return number + int(pid)\n\nprocess_data = [{\'pid\': item} for item in range(3)]\nresults = MPmq(function=do_work, process_data=process_data, shared_data={\'number\': 10}).execute()\nprint(f"Results: {\', \'.join(str(num) for num in results)}")\n ```\n\nExecuting the code above results in the following (for conciseness only INFO level messages are shown):\n\n```Python\nMainProcess [start_next_process] INFO started background process at offset:0 with id:862 name:Process-1\nProcess-1 [do_work] INFO hello from process: 0\nMainProcess [start_next_process] INFO started background process at offset:1 with id:863 name:Process-2\nMainProcess [start_next_process] INFO started background process at offset:2 with id:865 name:Process-3\nMainProcess [start_processes] INFO started 3 background processes\nProcess-2 [do_work] INFO hello from process: 1\nProcess-2 [_queue_handler] DEBUG adding \'do_work\' offset:1 result to result queue\nProcess-3 [do_work] INFO hello from process: 2\nProcess-2 [_queue_handler] DEBUG execution of do_work offset:1 ended\nProcess-2 [_queue_handler] DEBUG DONE\nProcess-3 [_queue_handler] DEBUG adding \'do_work\' offset:2 result to result queue\nMainProcess [complete_process] INFO process at offset:1 id:863 name:Process-2 has completed\nProcess-3 [_queue_handler] DEBUG execution of do_work offset:2 ended\nProcess-3 [_queue_handler] DEBUG DONE\nProcess-1 [_queue_handler] DEBUG adding \'do_work\' offset:0 result to result queue\nProcess-1 [_queue_handler] DEBUG execution of do_work offset:0 ended\nProcess-1 [_queue_handler] DEBUG DONE\nMainProcess [complete_process] INFO joining process at offset:1 with id:863 name:Process-2\nMainProcess [process_control_message] INFO the to process queue is empty\nMainProcess [complete_process] INFO process at offset:2 id:865 name:Process-3 has completed\nMainProcess [complete_process] INFO joining process at offset:2 with id:865 name:Process-3\nMainProcess [process_control_message] INFO the to process queue is empty\nMainProcess [complete_process] INFO process at offset:0 id:862 name:Process-1 has completed\nMainProcess [complete_process] INFO joining process at offset:0 with id:862 name:Process-1\nMainProcess [process_control_message] INFO the to process queue is empty\nMainProcess [run] INFO there are no more active processses - quitting\n>>> print(f"Results: {\', \'.join(str(num) for num in results)}")\nResults: 10, 11, 12\n```\n\n### Projects using `mpmq`\n\n* [`mpcurses`](https://pypi.org/project/mpcurses/) An abstraction of the Python curses and multiprocessing libraries providing function execution and runtime visualization capabilities\n\n* [`mppbars`](https://pypi.org/project/mppbar/) Scale execution of a function across multiple across a number of background processes while displaying their execution status via a progress bar\n\n* [`mp4ansi`](https://pypi.org/project/mp4ansi/) A simple ANSI-based terminal emulator that provides multi-processing capabilities\n\n### Development\n\nClone the repository and ensure the latest version of Docker is installed on your development server.\n\nBuild the Docker image:\n```sh\ndocker image build \\\n-t mpmq:latest .\n```\n\nRun the Docker container:\n```sh\ndocker container run \\\n--rm \\\n-it \\\n-v $PWD:/code \\\nmpmq:latest \\\nbash\n```\n\nExecute the build:\n```sh\npyb -X\n```\n',
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
        author_email = 'emilio.reyes@intel.com',
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
