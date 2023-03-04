#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.pylint")
use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.distutils")


NAME = "random-photo-viewer-telegram-bot"
DEFAULT_TASK = "publish"
