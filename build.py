"""   -*- coding: utf-8 -*-"""
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('python.pycharm')

NAME = "secure_all"
DEFAULT_TASK = "publish"


@init
def set_properties(project):
    """init"""
    pass
