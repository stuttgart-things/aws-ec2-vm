#!/usr/bin/env python3
import yaml
import random
from jinja2 import Template
import os
import argparse
import sys
import shutil

# WORKSPACE MODULE CALL TEMPLATE
moduleCallTemplate = """module "ec2-vm" {% raw %}{{% endraw %}{% for key in values %}
  {{ key }} = {{ values[key] }}{% endfor %}
}"""

stateS3Template = """terraform {
  backend "{{ values.name }}" {
    bucket = "{{ values.bucket }}"
    key    = "{{ values.key }}"
    region = "{{ values.region }}"
  }
}"""

outputsTemplate = """{%- for output in values.all %}{% set outputs = output.split('+') %}
output "{{ outputs[0] }}" {
  value = [module.{{ outputs[1] }}]
}{% endfor %}
"""

# PARSE ARGS
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--values', default='values.yaml')
parser.add_argument('-s', '--source', default='local')
parser.add_argument('-p', '--path', default='/tmp/tf/')
parser.add_argument('-st', '--state', default='local')

args = parser.parse_args()

local_module_path = os.path.dirname(sys.path[0])
module_name = local_module_path.split('/').pop()
local_workspace_path = args.path + module_name

# DIRECTORY CREATION & CHECK IF IT EXISTS OR NOT

# DELETE LOCAL WORKSPACE FOLDER IF EXISTS
if os.path.exists(local_workspace_path):
    shutil.rmtree(local_workspace_path)
    print("EXISTING FOLDER %s DELETED!" % local_workspace_path)

# CREATE WORKSPACE FOLDER
if not os.path.exists(local_workspace_path):
  os.makedirs(local_workspace_path)
  print("FOLDER %s CREATED!" % local_workspace_path)
else:
  print("FOLDER %s ALREADY EXISTS" % local_workspace_path)

# GET RANDOM ITEM FROM LIST
def get_random_fromlist(list):
  random_num = random.choice(list)
  print("RANDOM SELECT IS: " + str(random_num))

  return str(random_num)

# RENDER TEMPLATE
def render_template(template, values):
  template = Template(template)
  renderedModuleCall = template.render(values=values)

  return str(renderedModuleCall)

# WRITE TO DISK
def write_todisk(content, destination):
  with open(destination, 'w') as f:
    f.write(content)

def main():

  # LOAD YAML FILE
  with open(args.values, 'r') as f:
      values = yaml.load(f, Loader=yaml.SafeLoader)

  # ITERATE OVER THE VALUES DICTIONARY + GET RANDOM VALUE
  if args.source == "local":
    values['call']['source'] = '"'+local_module_path+'"'

  for key in values:

    # CHECK FOR LIST
    if isinstance(values[key], list):
      values[key] = get_random_fromlist(values[key])

  renderedModuleCall = render_template(moduleCallTemplate, values.get('call'))
  renderedModuleCall = renderedModuleCall.replace("True", "true")
  renderedModuleCall = renderedModuleCall.replace("False", "false")
  write_todisk(renderedModuleCall, local_workspace_path+'/main.tf')

  print(renderedModuleCall)

  if args.state == "s3":
     renderedStateConfig = render_template(stateS3Template, values.get('state'))
     print(renderedStateConfig)
     write_todisk(renderedStateConfig, local_workspace_path+'/state.tf')

  if "outputs" in values:
     renderedOutputs = render_template(outputsTemplate, values.get('outputs'))
     print(renderedOutputs)
     write_todisk(renderedOutputs, local_workspace_path+'/output.tf')

if __name__ == '__main__':
    main()
