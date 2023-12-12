# pylint: disable=invalid-name
# pylint: disable=protected-access
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import

from collections import defaultdict

from step_definitions.test_common import *
from step_definitions.test_assertions import *


def pytest_configure(config):
    config.option.keyword = "automated"
    config.option.markexpr = "not not_in_scope"
    pytest.globalDict = defaultdict()


def pytest_addoption(parser):
    parser.addoption("--tags", metavar="str", help="Will filter tests by given tags")
