from xml.etree.ElementTree import Comment


list1 = ["pears","apple","pineapple","fruit"]
#list1.append("stuff")
#list1.sort()
#print(list1)


set1 = set()

set1.add(1)
set1.add(2)
set1.add(3)
set1.add(3)
set1.add(4)
# In sets all elements are unique thus the 3 is added but not repeated
# print(set1, f"set1 contains {len(set1)} elements")
players = {"Joe root":"England", "Ben stokes":"England", "Steve Smith":"Australia", "Kane Williamson": "New Zealand"}
players["Mathew Wade"] = "Australia"
print(players["Kane Williamson"])
print(players["Mathew Wade"])