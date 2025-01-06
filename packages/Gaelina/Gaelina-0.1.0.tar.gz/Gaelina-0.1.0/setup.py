import os
import re
from setuptools import setup

tag = os.environ.get('CI_COMMIT_TAG')
branch = os.environ.get('CI_COMMIT_BRANCH')
version = tag or (branch if re.match(r'\d+\.\d+', branch) else '0.0')

if __name__ == '__main__':
    setup(
        version=version,
        long_description=open('README.md').read() + '\n\n\n' + open('CHANGELOG.md').read(),
        long_description_content_type='text/markdown'
    )
