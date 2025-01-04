from setuptools import setup, find_packages
setup(
      name='efftime',
      version='1.0.2',
      author='BreezeSun',
      description='A check Program run efficiency.',
      packages=find_packages(),
      long_description=open('README.md','r',encoding='utf-8').read(),
      long_description_content_type="text/markdown",
      license="MIT"
)

