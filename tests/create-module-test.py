#!/usr/bin/env python3
import yaml
import random
from jinja2 import Template

# GET RANDOM ITEM FROM LIST
def get_random_fromlist(list):
  random_num = random.choice(list)
  print("Random select is : " + str(random_num))

  return str(random_num)

# LOAD YAML FILE
with open('values.yaml', 'r') as f:
    values = yaml.load(f, Loader=yaml.SafeLoader)

# ITERATE OVER THE VALUES DICTIONARY + GET RANDOM VALUE
for key in values:
  print(key)

  if isinstance(values[key], list):
    values[key] = get_random_fromlist(values[key])

  print(values[key])

# name = input("Enter your name: ")

moduleCallTemplate = """module "ec2-vm" {% raw %}{{% endraw %}{% for key in values %}
  {{ key }}="{{ values[key] }}"{% endfor %}
}"""

tm = Template(moduleCallTemplate)
msg = tm.render(values=values)
print(msg)