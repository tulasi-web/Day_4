"""INPUT=LAYOUT

OUTPUT=OUT [USE – INDEXING]
OUTPUT=LAY [USE +INDEXING]
OUPUT=LAYOUT [USE -INDEXING]
OUTPUT=TUOAYL [USE + INDEXING]
OUTPUT=YOU [USE + INDEXING]
OUTPUT=YOU [USE – INDEXING]
"""
i="LAYOUT"
print(i[-3::1])
print(i[:3])
print(i[-6::1])
print("AYL slicing wont work")
print(i[2:5:1])
print(i[-4:-1:1])
