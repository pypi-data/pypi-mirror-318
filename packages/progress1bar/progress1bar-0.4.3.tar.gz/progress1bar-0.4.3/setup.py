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
        name = 'progress1bar',
        version = '0.4.3',
        description = 'A customizable ANSI-based progress bar',
        long_description = "# progress1bar\n[![build](https://github.com/soda480/progress1bar/actions/workflows/main.yml/badge.svg)](https://github.com/soda480/progress1bar/actions/workflows/main.yml)\n[![complexity](https://img.shields.io/badge/complexity-A-brightgreen)](https://radon.readthedocs.io/en/latest/api.html#module-radon.complexity)\n[![coverage](https://img.shields.io/badge/coverage-96%25-brightgreen)](https://pybuilder.io/)\n[![vulnerabilities](https://img.shields.io/badge/vulnerabilities-None-brightgreen)](https://pypi.org/project/bandit/)\n[![PyPI version](https://badge.fury.io/py/progress1bar.svg)](https://badge.fury.io/py/progress1bar)\n[![python](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-teal)](https://www.python.org/downloads/)\n\nA customizable ANSI-based progress bar.\n\n## Installation\n```bash\npip install progress1bar\n```\n\n### `ProgressBar`\n\n```\nProgressBar(\n    total=None,\n    fill=None,\n    regex=None,\n    completed_message=None,\n    clear_alias=False,\n    show_prefix=True,\n    show_fraction=True,\n    show_percentage=True,\n    show_duration=False,\n    show_complete=True,\n    ticker=None,\n    use_color=True,\n    show_bar=True)\n```\n\n<details><summary>Documentation</summary>\n\n> `total` - An integer for the total number of items the progress bar will show that need to be completed.\n\n> `fill` - A dictionary whose key values are integers that dictate the number of leading zeros the progress bar should add to the `total` and `completed` values; this is optional and should be used to format the progress bar appearance. The supported key values are `max_total` and `max_completed`.\n\n> `regex` - A dictionary whose key values are regular expressions for `total`, `count` and `alias`. The regular expressions will be checked against the log messages intercepted from the executing function, if matched the value will be used to assign the attribute for the respective progress bar. The `total` and `count` key values are required, the `alias` key value is optional.\n\n> `completed_message` - A string to designate the message the progress bar should display when complete. Default is 'Processing complete'\n\n> `clear_alias` - A boolean to designate if the progress bar should clear the alias when complete.\n\n> `show_prefix` - A boolean to designate if the prefix of `Processing ` should be printed prefixing the progress bar.\n\n> `show_fraction` - A boolean to designate if the fraction should be printed with the progress bar.\n\n> `show_percentage` - A boolean to designate if the percentage should be printed with the progress bar.\n\n> `show_duration` - A boolean to designate if the duration should be printed after progress bar execution.\n\n> `show_complete` - A boolean to designate if the completed message is to be displayed upon progress bar completion.\n\n> `ticker` - A integer representing unicode character to print as the progress bar ticker. Refer to [unicode chart](https://www.ssec.wisc.edu/~tomw/java/unicode.html) for values. Default is 9632 (black square ■).\n\n> `use_color` - A boolean to designate if the progress bar should be displayed with color. Default is `True`.\n\n> `show_bar` - A boolean to designate if the progress bar tickers should be printed.\n\n**Attributes**\n\n> `count` - An integer attribute to increment that designates the current count. When count reaches total the progress bar will show complete.\n\n> `alias` - A string attribute to set the alias of the progress bar.\n\n**Functions**\n\n> **reset()**\n>> Reset the progress bar so that it can be used again. It will maintain and show the number of times the progress bar has been used.\n\n</details>\n\n\n### Examples\n\nVarious [examples](https://github.com/soda480/progress1bar/tree/master/examples) are included to demonstrate the progress1bar package. To run the examples, build the Docker image and run the Docker container using the instructions described in the [Development](#development) section.\n\n#### [example1](https://github.com/soda480/progress1bar/tree/master/examples/example1.py)\n\nThe `ProgressBar` class is used to display function execution as a progress bar. Use it as a context manager, and simply set the `.total` and `.count` attributes accordingly. Here is an example:\n\n```Python\nimport time\nfrom progress1bar import ProgressBar\n\nwith ProgressBar(total=250) as pb:\n    for _ in range(pb.total):\n        pb.count += 1\n        # simulate work\n        time.sleep(.01)\n```\n\n![example](https://raw.githubusercontent.com/soda480/progress1bar/master/docs/images/example1.gif)\n\n#### [example2](https://github.com/soda480/progress1bar/tree/master/examples/example2.py)\n\nConfigure `ProgressBar` to display an alias for the item that is currently being processed by setting the `alias` parameter:\n\n```Python\nimport time\nfrom faker import Faker\nfrom progress1bar import ProgressBar\n\nkwargs = {\n    'total': 75,\n    'completed_message': 'Processed names complete',\n    'clear_alias': True,\n    'show_fraction': False,\n    'show_prefix': False,\n    'show_duration': True\n}\nwith ProgressBar(**kwargs) as pb:\n    for _ in range(pb.total):\n        pb.alias = Faker().name()\n        # simulate work\n        time.sleep(.08)\n        pb.count += 1\n```\n\n![example](https://raw.githubusercontent.com/soda480/progress1bar/master/docs/images/example2.gif)\n\n#### [example2b](https://github.com/soda480/progress1bar/tree/master/examples/example2b.py)\n\nConfigure `ProgressBar` to display an alias for the item that is currently being processed, but do not print out the ticker, instead show percentage and fraction complete:\n\n```Python\nfrom faker import Faker\nfrom progress1bar import ProgressBar\n\nkwargs = {\n    'total': 575,\n    'clear_alias': True,\n    'show_complete': False,\n    'show_prefix': False,\n    'show_duration': True,\n    'show_bar': False\n}\nwith ProgressBar(**kwargs) as pb:\n    for _ in range(pb.total):\n        pb.alias = Faker().sentence()\n        # simulate work\n        pb.count += 1\n```\n\n![example](https://raw.githubusercontent.com/soda480/progress1bar/master/docs/images/example2b.gif)\n\n\n#### [example3](https://github.com/soda480/progress1bar/tree/master/examples/example3.py)\n\nConfigure `ProgressBar` with a custom ticker, show duration, do not use color, and use regular expressions to determine the `total`, `count` and `alias` attributes:\n\n```Python\nimport random\nfrom faker import Faker\nfrom progress1bar import ProgressBar\n\nkwargs = {\n    'ticker': 9733,\n    'regex': {\n        'total': r'^processing total of (?P<value>\\d+)$',\n        'count': r'^processed .*$',\n        'alias': r'^processor is (?P<value>.*)$'\n    },\n    'use_color': False,\n    'show_duration': False\n}\nwith ProgressBar(**kwargs) as pb:\n    pb.match(f'processor is {Faker().name()}')\n    total = random.randint(500, 750)\n    pb.match(f'processing total of {total}')\n    for _ in range(total):\n        pb.match(f'processed {Faker().name()}')\n\n```\n\n![example](https://raw.githubusercontent.com/soda480/progress1bar/master/docs/images/example3.gif)\n\n#### [example4](https://github.com/soda480/progress1bar/tree/master/examples/example4.py)\n\nConfigure `ProgressBar` to show and reuse progress for several iterations:\n\n```Python\nimport random\nimport time\nfrom faker import Faker\nfrom progress1bar import ProgressBar\n\nTOTAL_ITEMS = 300\nITERATIONS = 4\nkwargs = {\n    'show_prefix': False,\n    'show_fraction': False,\n    'show_duration': True\n}\nprint(f'Execute {ITERATIONS} iterations of varying totals:')\nwith ProgressBar(**kwargs) as pb:\n    iterations = 0\n    while True:\n        if iterations == ITERATIONS:\n            pb.alias = ''\n            pb.complete = True\n            break\n        pb.alias = Faker().name()\n        pb.total = random.randint(100, TOTAL_ITEMS)\n        for _ in range(pb.total):\n            Faker().name()\n            pb.count += 1\n        iterations += 1\n        pb.reset()\n        time.sleep(.4)\n```\n\n![example](https://raw.githubusercontent.com/soda480/progress1bar/master/docs/images/example4.gif)\n\n### Programs using `progress1bar`\n\n* [pypbars](https://pypi.org/project/pypbars/)\n* [mppbar](https://pypi.org/project/mppbar/)\n\n## Development ##\n\nClone the repository and ensure the latest version of Docker is installed on your development server.\n\nBuild the Docker image:\n```sh\ndocker image build \\\n-t progress1bar:latest .\n```\n\nRun the Docker container:\n```sh\ndocker container run \\\n--rm \\\n-it \\\n-v $PWD:/code \\\nprogress1bar:latest \\\nbash\n```\n\nExecute the build:\n```sh\npyb -X\n```\n",
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

        url = 'https://github.com/soda480/progress1bar',
        project_urls = {},

        scripts = [],
        packages = ['progress1bar'],
        namespace_packages = [],
        py_modules = [],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = [
            'cursor',
            'colorama'
        ],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        python_requires = '',
        obsoletes = [],
    )
