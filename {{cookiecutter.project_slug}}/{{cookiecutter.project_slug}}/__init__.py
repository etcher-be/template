# coding=utf-8
"""
Top-level package for {{ cookiecutter.project_name }}.
"""

import sys

from pkg_resources import DistributionNotFound, get_distribution

try:
	__version__ = get_distribution('{{ cookiecutter.project_slug }}.').version
except DistributionNotFound:  # pragma: no cover
	# package is not installed
	__version__ = 'not installed'
	
__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
