sugang = dict(python="kim", cpp="sung", db="kang")
# print(sugang)
sugang['datastructure'] = 'kim'     #add
# print(sugang)
sugang['datastructure'] = 'park'    #update
print(sugang)
print(sugang["db"])
print(sugang.get('db'))
print(sugang.get('opensource'))
print(sugang.get('opensource', 'not exist'))
print(sugang.items())
print(sugang.keys())
print(sugang.values())