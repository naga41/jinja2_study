# -*- coding: utf-8 -*-
import os
import yaml

import jinja2

OUTPUT_DIR = './output'
TEMPLATE_DIR = './templates'
PARAMS='./app.yml'


def build_templates(template_dir, dict_vars):

    template_loader = jinja2.FileSystemLoader(template_dir)
    template_env = jinja2.Environment(loader=template_loader)

    for template in template_env.list_templates(extensions='.j2'):
        rendered_string = template_env.get_template(template).render(dict_vars)
        output_renderd_file(template, rendered_string)


def load_template_params(parameter_file):
    with open(parameter_file) as f:
        params = yaml.load(f)
    return params


def output_renderd_file(template_file_path, file_contents):
    output_path = OUTPUT_DIR + '/' + os.path.splitext(template_file_path)[0]
    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))
    with open(output_path, 'w') as f:
        f.write(file_contents)

if __name__ == "__main__":
    template_params = load_template_params(PARAMS)
    build_templates(TEMPLATE_DIR, template_params)