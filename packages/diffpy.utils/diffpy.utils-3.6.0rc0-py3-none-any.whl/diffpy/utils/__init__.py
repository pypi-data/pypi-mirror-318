#!/usr/bin/env python
##############################################################################
#
# (c) 2024 The Trustees of Columbia University in the City of New York.
# All rights reserved.
#
# File coded by: Billinge Group members and community contributors.
#
# See GitHub contributions for a more detailed list of contributors.
# https://github.com/diffpy/diffpy.utils/graphs/contributors
#
# See LICENSE.rst for license information.
#
##############################################################################
"""Shared utilities for diffpy packages."""

# package version
from diffpy.utils.version import __version__

# silence the pyflakes syntax checker
assert __version__ or True
