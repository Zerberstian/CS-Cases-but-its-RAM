import json

with open('RAM.json', 'r', encoding='utf-8') as f:
  RAM_Riegel = json.load(f)

class RAM:
  def __init__(self, name):
    self.name = name
    for i in RAM_Riegel:
      if i 
