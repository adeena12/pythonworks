#nested dictionary
dict={"a":{"name":"adeena","age":12,"course":"python"},"b":{"address":"abc","frm":"efg"}}

print(dict)
print(type(dict))
print(dict["a"]["name"])
dict["c"]={"fruit":"orange"}
print(dict["c"])
print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())
dict.update({"d":{"frut":"apple"}})
print(dict)
dict.popitem()
print(dict)
dict.pop("c")
print(dict)

