
import re
data = dir(re)
result = [i for i in data if i.startswith('find')]
print(result)



find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))