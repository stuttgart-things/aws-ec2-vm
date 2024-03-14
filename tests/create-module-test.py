#!/usr/bin/env python3
import yaml
import random
from jinja2 import Template
import os
import sys


# DIRECTORY CREATION & CHECK IF IT EXISTS OR NOT
path = "/tmp/aws-ec2-vm"

if not os.path.exists(path):
  os.mkdir(path)
  print("Folder %s created!" % path)
else:
  print("Folder %s already exists" % path)


# TEMPLATE
moduleCallTemplate = """module "ec2-vm" {% raw %}{{% endraw %}{% for key in values %}
  {{ key }}="{{ values[key] }}"{% endfor %}
}"""

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
  with open('values.yaml', 'r') as f:
      values = yaml.load(f, Loader=yaml.SafeLoader)

  # ITERATE OVER THE VALUES DICTIONARY + GET RANDOM VALUE
  for key in values:

    # CHECK FOR LIST
    if isinstance(values[key], list):
      values[key] = get_random_fromlist(values[key])

  renderedTemplate = render_template(values)
  print(renderedTemplate)

# ADDING DIFFERENT PATH TO GET THE RENDERED TEMPLATE
#  if len(sys.argv) > 1:
#    new_output_path = sys.argv[1]
#  else:
#    print("Please provide the output path as an argument.")
#    sys.exit(1)
#  output_path = new_output_path
#
#  output_file = open(output_path, "w")
#  output_file.write(renderedTemplate)
#  output_file.close()


#render output
  with open(path+'/main.tf', 'w') as f:              ### used concatenation here ###
    f.write(renderedTemplate)

if __name__ == '__main__':
    main()
