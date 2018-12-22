from contextlib import contextmanager
import shlex
import os
import subprocess
from cookiecutter.utils import rmtree
from logging import Logger


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Delete the temporal directory that is created when executing the tests
    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    "Run a command from inside a given directory, returning the command output"
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def project_info(result):
    """Get toplevel dir, app_name, and project dir from baked cookies"""
    project_path = str(result.project)
    app_name = os.path.split(project_path)[-1]
    project_dir = os.path.join(project_path, app_name)
    return project_path, app_name, project_dir


def test_bake_with_defaults(cookies, logger: Logger):
    logger.debug("Baking with default values")
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert 'setup.py' in found_toplevel_files
        assert 'tox.ini' in found_toplevel_files
        assert 'tests' in found_toplevel_files
        assert 'docs' in found_toplevel_files


def test_bake_and_run_tests(cookies, logger: Logger):
    logger.debug("Running Bake with Default Values and Unit Test on rendered content\n")
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        logger.debug("Path Used for Running Unit Test on rendered content {}\n".format(str(result.project)))
        if not os.getenv("SKIP_TESTS"):
            assert run_inside_dir('python setup.py test', str(result.project)) == 0


def test_bake_withspecialchars_and_run_tests(cookies, logger: Logger):
    logger.debug("Testing Maintainer with doubele quote Characters")
    with bake_in_temp_dir(cookies, extra_context={'maintainer': 'name "quote" name'}) as result:
        assert result.project.isdir()
        logger.debug("Path Used for Running Unit Test on rendered content {}\n".format(str(result.project)))
        if not os.getenv("SKIP_TESTS"):
            assert run_inside_dir('python setup.py test', str(result.project)) == 0


def test_bake_with_apostrophe_and_run_tests(cookies, logger: Logger):
    logger.debug("Testing Maintainer with apostrophes Characters")
    with bake_in_temp_dir(cookies, extra_context={'full_name': "O'connor"}) as result:
        assert result.project.isdir()
        logger.debug("Path Used for Running Unit Test on rendered content {}\n".format(str(result.project)))
        if not os.getenv("SKIP_TESTS"):
            assert run_inside_dir('python setup.py test', str(result.project)) == 0
