#samples
dict={"name":"adeena","age":12,"course":"python"}
print(dict)
print(type(dict))
print(dict["name"])
#or
print(dict.get("name"))
print(dict.keys())
print(dict.values())
print(dict.items())
dict ["age"]= 34  #to change
print(dict)
dict.update({"age":23,"name":"amr"})
print(dict)
dict.update({"new":"chr"})
print(dict)
dict["color"]="red"  #adding
print(dict)
dict.pop("new")  #to remove
print(dict)
dict.popitem()  #remove last item
print(dict)
del dict["course"]  #deleting
print(dict)
#dict.clear()
#print(dict)
dict.copy()
print(dict)

for i in dict.values():
    print(i)
