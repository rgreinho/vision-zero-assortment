import pathlib

from jinja2 import Environment
from jinja2 import FileSystemLoader

MAIL_TEMPLATE = """
"""


def file_to_string(template_file, vars):
    j2_env = Environment(
        loader=FileSystemLoader(str(pathlib.Path(".").absolute())), trim_blocks=True
    )
    return j2_env.get_template(template_file).render(vars)


def var_to_string(vars):
    return Environment().from_string(MAIL_TEMPLATE).render(vars)
