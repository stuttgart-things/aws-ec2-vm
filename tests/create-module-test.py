#!/usr/bin/env python3
import yaml
import random
from jinja2 import Template
import os

# Directory
directory = "aws-ec2-vm"
parent_dir = "/tmp/"
path = os.path.join(parent_dir, directory)
os.mkdir(path) 
print("Directory '% s' created" % directory) 


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

if __name__ == '__main__':
    main()