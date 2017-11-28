#!/bin/python

#
# Modified  source code by Aleksandr Mattal (qute.bits@gmail.com) at https://github.com/qutebits/resume_tex.py
# into mkresume.py
#

import argparse
import re
import yaml
import sys

from datetime import date
from jinja2 import Environment, FileSystemLoader


#this_loc = len(open("resume_tex.py", 'r').readlines()) #lets keep it at 42

def generate(yaml_file,template_path,header_file,body_file):

  print("%#DATE GENERATED",date.today().strftime("%B %d, %Y")) 
  print("%#YAML input=",yaml_file)
  print("%#TEMPLATE path=",template_path)
  print("%#HEADER file=",header_file,", located in ",template_path)
  print("%#BODY file=",body_file,", located in",template_path)
  
  yaml_contents = yaml.load(open(yaml_file, 'r')) ###################################LOAD YAML FILE
  env = Environment(loader=FileSystemLoader(template_path), #########################LOAD TEMPLATE DIR
  block_start_string='~{',block_end_string='}~',
  variable_start_string='~{{', variable_end_string='}}~') 

  body = ""
  for section in yaml_contents['order']: #generate sections 1 by 1
    contents = yaml_contents[section[0]]
    name = section[1].title()
    body += env.get_template(body_file).render(   ######################################LOAD BODY FILE
      name = name.upper(),
      contents = contents
    )
  #and then generate the TeX wrapper and fill it with generated sections
 # result = open("RESULT.tex", 'w')
  #result.write
  print(env.get_template(header_file).render(    ############################3# LOAD HEADER FILE
    name = yaml_contents['name'].upper(),
    email = yaml_contents['email'],
 #  loc = this_loc, #lines of code in this very script :)
    body = body,
    today = date.today().strftime("%B %d, %Y") #generation date
  ))
  #result.close()


def main():
    parser = argparse.ArgumentParser(description='Generates LaTeX resumes from data in YAML files. Latex file is written to STDOUT')
    parser.add_argument('-y','--yaml',metavar='INYAML',required=True,help='The local YAML file or its \"path/filename\"')
    parser.add_argument('-t','--tpath',metavar='IN_TEMPLATE',required=True,help='The path of the template directory that contains the templates')
    parser.add_argument('-H','--header',metavar='INHEADER',required=True,help='The \"header template\"  templatefile')
    parser.add_argument('-b','--body',metavar='INBODY',required=True,help='The \"body template\" templatefile')
    
    args = parser.parse_args()
    #print(args)
    generate(args.yaml,args.tpath,args.header,args.body)

if __name__ == "__main__":
        main()
