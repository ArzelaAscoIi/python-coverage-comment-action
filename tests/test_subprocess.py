import pytest

from coverage_comment import subprocess


def test_run__ok():
    subprocess.run("echo", "yay").stdout == "yay"


def test_run__kwargs():
    subprocess.run("pwd", cwd="/").stdout == "/"


def test_run__error():
    with pytest.raises(subprocess.SubProcessError):
        subprocess.run("false")
