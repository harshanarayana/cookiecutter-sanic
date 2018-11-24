from pexpect import spawn
from os import getcwd, path, makedirs
import logging
import sys
from collections import OrderedDict

logger = logging.getLogger("test")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
logger.addHandler(ch)

cookiecutter_template_path = path.join(
    path.dirname(getcwd()), "cookiecutter-sanic")
output_path = path.join(
    path.dirname(cookiecutter_template_path), "output")

expect_to_arg_map = OrderedDict({
    "repo_name [sanic-skeleton]: ": "sanic-test",
    "app_name [sanic_skeleton]": "sanic_test",
    "run [run]": "run",
    "enable_swagger": "y",
    "sanic_env_prefix": "SANIC_",
    "sanic_port": "8000",
    "sanic_host": "0.0.0.0",
    "maintainer": "some random test maintainer",
    "Select tox_env": "2",
    "Select enable_codecov": "2",
    "Select run_mode:": "1",
    "workers": "4",
    "Select enable_auto_reload": "1"
})

# Setup Directory path for output
if not path.isdir(output_path):
    makedirs(output_path)


cookiecutter_command = "cookiecutter {} -o {}" \
    .format(cookiecutter_template_path, output_path)

logger.debug("Command being executed to Test Template Rendering: {}"
             .format(cookiecutter_command))

child = spawn(cookiecutter_command)
child.logfile = sys.stdout.buffer
if child.exitstatus:
    logger.error(child.stderr)
    raise Exception

for expected_value, input_answer in expect_to_arg_map.items():
    logger.debug("Expecting : {}".format(expected_value))
    child.expect_exact([expected_value])
    child.sendline(input_answer)

child.read()
child.wait()

if child.exitstatus:
    logger.error("Failed to Run cookiecutter Commands")
    logger.error(child.stderr)
    raise Exception
