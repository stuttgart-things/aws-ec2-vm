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
  {{ key }} = {% if ("True" == values[key]) or ("False" == values[key]) or ("[" == values[key][0]) %}{{ values[key] }}{% else %}"{{ values[key] }}"{% endif %}{% endfor %}
}"""

# S3 STATE CONFIGURATION TEMPLATE
stateS3Template = """terraform {
  backend "{{ values.name }}" {
    bucket = "{{ values.bucket }}"
    key    = "{{ values.key }}"
    region = "{{ values.region }}"
  }
}"""

# OUTPUTS TEMPLATE
outputsTemplate = """{%- for output in values.all %}{% set outputs = output.split('+') %}
output "{{ outputs[0] }}" {
  value = [{{ outputs[1] }}]
}{% endfor %}
"""

# NOTES TEMPLATE
notesTemplate = """
HOW TO EXECUTE TERRAFORM:
terraform -chdir="{{ values.workspace_path }}" init --upgrade \
&& terraform -chdir="{{ values.workspace_path }}" plan \
&& terraform -chdir="{{ values.workspace_path }}" apply --auto-approve
"""

# PARSE ARGS
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--values', default='values.yaml')
parser.add_argument('-s', '--source', default='local')
parser.add_argument('-p', '--path', default='/tmp/tf/')
parser.add_argument('-st', '--state', default='local')
# PLEASE ADD AN ARGUMENT FOR OVERWRITES                  ANKIT TO DO              
args = parser.parse_args()


# SET WORSPACE VARS
local_module_path = os.path.dirname(sys.path[0])
module_name = local_module_path.split('/').pop()
local_workspace_path = args.path + module_name

def create_workspace():

  # DELETE LOCAL WORKSPACE FOLDER IF EXISTS
  if os.path.exists(local_workspace_path):
      shutil.rmtree(local_workspace_path)
      print("EXISTING FOLDER %s DELETED!" % local_workspace_path)

  # CREATE WORKSPACE FOLDER
  if not os.path.exists(local_workspace_path):
    os.makedirs(local_workspace_path)
    print("FOLDER %s CREATED!" % local_workspace_path)

# GET RANDOM ITEM FROM LIST
def get_random_fromlist(list):
  random_num = random.choice(list)
  print("RANDOM SELECT IS: " + str(random_num))

  return str(random_num)

# UPDATE_DICT & MERGE FUNCTIONS HERE                     ANKIT TO DO
def update_dict_with_overwrites(input_dict, overwrite_string):
    pairs = overwrite_string.split(';')
    for pair in pairs:
        key, value = pair.split('=')
        input_dict[key.strip()] = value.strip()
    return input_dict

# MERGE FUNCTION
def merge(input_dict, my_dict):
    res = input_dict | my_dict
    return res
  
# RENDER TEMPLATE
def render_template(template, values):
  template = Template(template)
  renderedModuleCall = template.render(values=values)

  return str(renderedModuleCall)

# WRITE TO DISK
def write_todisk(content, destination):
  with open(destination, 'w') as f:
    f.write(content)

def pick_random(values):
  for key in values:
    # CHECK FOR LIST
    if isinstance(values[key], list):
      values[key] = get_random_fromlist(values[key])

  return values

def main():

  # CREATE LOCAL WORKSPACE
  create_workspace()

  # LOAD YAML FILE
  with open(args.values, 'r') as f:
      values = yaml.load(f, Loader=yaml.SafeLoader)
    
## CHECK IF ARGS OVERWRITES ARE SET, IF SOME OVERWRITES ARE SET -> CALL UPDATED_DICTS FUNCTION
  
  # ITERATE OVER THE VALUES DICTIONARY + GET RANDOM VALUE
  if args.source == "local":
    values['call']['source'] = local_module_path

  # GET RANDOM VALUES
  randomValues = pick_random(values.get('call'))

  # RENDER MODULE CALL
  
  # PLEASE MERGE WITH OVERWRTIES DICTS   -> CALL TO MERGE DICT FUNCTION BEFORE RENDER                  ANKIT TO DO
  
  renderedModuleCall = render_template(moduleCallTemplate, randomValues)
  renderedModuleCall = renderedModuleCall.replace("True", "true")
  renderedModuleCall = renderedModuleCall.replace("False", "false")

  # PRINT MODULE CALL
  print(renderedModuleCall)

  # WRITE MODULE CALL TO DISK
  write_todisk(renderedModuleCall, local_workspace_path+'/main.tf')

  if args.state == "s3":
    # PLEASE MERGE WITH OVERWRTIES DICTS                                    ANKIT TO DO
     renderedStateConfig = render_template(stateS3Template, values.get('state'))

     # PRINT STATE CONFIG
     print(renderedStateConfig)

     # WRITE MODULE CALL TO DISK
     write_todisk(renderedStateConfig, local_workspace_path+'/state.tf')

  if "outputs" in values:
     renderedOutputs = render_template(outputsTemplate, values.get('outputs'))

     # PRINT OUTPUTS
     print(renderedOutputs)

     # WRITE OUTPUTS TO DISK
     write_todisk(renderedOutputs, local_workspace_path+'/output.tf')

  # PRINT TERRAFORM INSTRUCTIONS/NOTES
  notes = {
  "workspace_path": local_workspace_path
  }

  renderedNotes = render_template(notesTemplate, notes)
  print(renderedNotes)


if __name__ == '__main__':
    main()
