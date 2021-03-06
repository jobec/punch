import pytest

pytestmark = pytest.mark.slow

version_file_content = """
major = 1
minor = 0
patch = 0
"""

config_file_content = """
__config_version__ = 1

GLOBALS = {
    'serializer': '{{major}}.{{minor}}.{{patch}}',
}

FILES = ["README.md"]

VERSION = ['major', 'minor', 'patch']
"""


def test_update_major(test_environment):
    test_environment.ensure_file_is_present("README.md", "Version 1.0.0")

    test_environment.ensure_file_is_present("punch_version.py", version_file_content)

    test_environment.ensure_file_is_present("punch_config.py", config_file_content)

    test_environment.call(["punch", "--part", "major"])

    assert test_environment.get_file_content("README.md") == "Version 2.0.0"


def test_update_minor(test_environment):
    test_environment.ensure_file_is_present("README.md", "Version 1.0.0")

    test_environment.ensure_file_is_present("punch_version.py", version_file_content)

    test_environment.ensure_file_is_present("punch_config.py", config_file_content)

    test_environment.call(["punch", "--part", "minor"])

    assert test_environment.get_file_content("README.md") == "Version 1.1.0"


def test_update_patch(test_environment):
    test_environment.ensure_file_is_present("README.md", "Version 1.0.0")

    test_environment.ensure_file_is_present("punch_version.py", version_file_content)

    test_environment.ensure_file_is_present("punch_config.py", config_file_content)

    test_environment.call(["punch", "--part", "patch"])

    assert test_environment.get_file_content("README.md") == "Version 1.0.1"
