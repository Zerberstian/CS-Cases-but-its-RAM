import json

with open('RAM.json', 'r', encoding='utf-8') as f:
  RAM_Riegel = json.load(f)

class RAM:
  def __init__(self, name):
    self.name = name
    for i in RAM_Riegel:
      if i ['ID] == id:
        self.category = i['category']
        self.size = i['size']
        self.Price = i['Price']
