#dictionaries

marks = {"joe": [8,9,10],"jojo": [10,11,12],"jane": [12,13,14],"john": [12,13,14]}

print(marks["joe"])
print(marks["jojo"])
print(marks["jane"][0])
print(marks["john"][2])
marks["paul"] = [15,16,17]
print(marks)
print("hello world")
marks.update({"peter":[15,16,17],"simon":[15,16,17],"kali":[15,16,17]})
print(marks)

del marks["joe"][0]
print(marks["joe"])

marks["joe"].append(11)
print(marks["joe"])
marks["joe"].extend([121,31,41])
marks["joe"].sort()
print(marks["joe"])