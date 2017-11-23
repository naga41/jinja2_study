# -*- coding: utf-8 -*-
import yaml

import jinja2

TEMPLATE_DIR = './templates'
PARAMS='./app.yml'


def load_template_params(parameter_file):
    with open(parameter_file) as f:
        params = yaml.load(f)
    return params


def build_templates(template_dir, dict_vars):

    template_loader = jinja2.FileSystemLoader(template_dir)
    template_env = jinja2.Environment(loader=template_loader)

    for template in template_env.list_templates(extensions='.j2'):
        print template_env.get_template(template).render(dict_vars)

if __name__ == "__main__":
    template_params = load_template_params(PARAMS)
    build_templates(TEMPLATE_DIR, template_params)