my=["Shumakova","Pavlova","Korneva","Niculin","Gorbacheva","Faradjeva","Shakirov","Barchenkov","Shevchenko","Pishikova"]
other=["Petrov","Ivanov","Sidorov","Treen","Freen","Kreen","Preen","Green","Vreen","Leen"]
import random
group_1=random.sample(my,5)
group_2=random.sample(other,5)
sport_team=tuple(group_1+group_2)
print("Group 1",my)
print("Group 2",other)
print("Sport team",sport_team)
print(len(sport_team))
sorted_team=sorted(sport_team)
print("Sorted team",sorted_team)
if "Ivanov" in sport_team:
    print("Ivanov part of team")
else:
    print("Ivanov not in team")
ivanov_count=sport_team.count("Ivanov")
print("Ivanov count",ivanov_count)

