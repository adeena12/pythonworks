import json
"""import os

print(dir(os))"""

x='{"adeena","diya"}'
print(type(x))
#parsing json to python
y = json.dumps(x)
print(type(y))

#y = json.loads(x)
#print(type(y))