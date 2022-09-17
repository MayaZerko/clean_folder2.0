from setuptools import setup, find_namespace_packages

setup(name='clean',
      version='1.0',
      description='Сортує задану папку- перевіряє внутрішні вкладення/ Форматує утворюючи нові папки і розархивовує архіви, також переіменовує.',
      url='https://github.com/MayaZerko/clean_folder',
      author='MayaZerko',
      author_email='',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']})
