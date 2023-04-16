#!/usr/bin/python

# Inspired by thesource code from Aleksandr Mattal:
# https://github.com/QuteBits/resume_42

#===============================================================================
# Imports
#===============================================================================

import sys
import os
from datetime import date

import re
from jinja2 import Environment, FileSystemLoader

import argparse
import yaml

#===============================================================================
# Internal functions
#===============================================================================

def main():
    parser = argparse.ArgumentParser(
               description='Generates LaTeX output from Jinja2 tex template.\
                            Latex file is written to STDOUT')
    parser.add_argument(
      '-y',
      '--yaml',
      metavar = 'YAML',
      required = True,
      help = 'The path of the YAML file filling the LaTex Jinja2 template')

    parser.add_argument(
      '-l',
      '--latex-template',
      metavar = 'LATEX_TEMPLATE',
      required = True,
      help = 'The path of the LaTeX Jinja2 template.')

    args = parser.parse_args()
    generate(args.yaml, args.latex_template)

def path_of(file_path):
    dirname = os.path.dirname(file_path)
    result = dirname if (dirname != '') else "./"
    return result

def generate(yaml_file, latex_template):

    template_path = path_of(latex_template)
    template_file = os.path.basename(latex_template)

    yaml_contents = yaml.safe_load(open(yaml_file, 'r'))

    env = Environment(
            loader = FileSystemLoader(template_path),
            block_start_string = '~{', block_end_string='}~',
            variable_start_string = '~{{', variable_end_string='}}~')

    body = ""

    today = date.today().strftime("%B %d, %Y")

    section_contents = {}
    section_names = []
    for section in yaml_contents['order']:
      section_name = section[1].title().upper() 
      section_names.append(section_name)
      section_contents[section_name] = yaml_contents[section[0]]

    print(env.get_template(template_file).render(
            name = yaml_contents['name'].upper(),
            email = yaml_contents['email'],
            section_names = section_names,
            section_contents = section_contents,
            today = today))

#===============================================================================
# Main entrypoint
#===============================================================================

if __name__ == "__main__":
    main()
