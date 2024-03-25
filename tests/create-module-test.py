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

# PARSE ARGS
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--values', default='values.yaml')
parser.add_argument('-s', '--source', default='local')
parser.add_argument('-p', '--path', default='/tmp/tf/')
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
def render_template(values):
  template = Template(moduleCallTemplate)
  renderedTemplate = template.render(values=values)

  return str(renderedTemplate)

def main():

  # LOAD YAML FILE
  with open(args.values, 'r') as f:
      values = yaml.load(f, Loader=yaml.SafeLoader)

  # ITERATE OVER THE VALUES DICTIONARY + GET RANDOM VALUE
  if args.source == "local":
    values["source"] = '"'+local_module_path+'"'

  for key in values:

    # CHECK FOR LIST
    if isinstance(values[key], list):
      values[key] = get_random_fromlist(values[key])

  renderedTemplate = render_template(values)
  renderedTemplate = renderedTemplate.replace("True", "true")
  renderedTemplate = renderedTemplate.replace("False", "false")

  print(renderedTemplate)

# RENDER OUTPUT
  with open(local_workspace_path+'/main.tf', 'w') as f:
    f.write(renderedTemplate)

if __name__ == '__main__':
    main()
