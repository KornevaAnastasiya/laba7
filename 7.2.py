dnf=[3,5,7,2,9,4,0,5,3,4,67,23]
dup=set()
oth=set()
for element in dnf:
    if element in oth:
        dup.add(element)
    else:
        oth.add(element)
if dup:
    print("Повторяющиеся элементы: ",*dup)
    print("Список", dnf)
else:
    print("Список",dnf)