#Two hardcoded lists of programming languages.
proglang1 = {"Python", "JavaScript", "SQL", "GO", "C"}
proglang2 = {"Python", "JavaScript", "HTML", "Swift"}
#Programming languages converted to a set.
set1 = set(proglang1)
set2 = set(proglang2)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
