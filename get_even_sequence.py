import json
import operator

full_arrange = {}
with open("./full_arrange.json","r") as json_f:
    full_arrange=json.load(json_f)

even_sequence={}
index = 0
for k,v in full_arrange.items():
    tmp = v[:]
    v.remove(0)
    counter = 0
    for i in range(8):
        for j in range(i,8):
            if v[i] > v[j]:
                counter += 1
    if counter % 2 == 0:
        if operator.eq(tmp,[1,2,3,4,5,6,7,8,0]):
            continue
        even_sequence[index] = tmp
        index += 1

with open("./even_sequence_result.json","w") as ff:
    json.dump(even_sequence,ff)
    print("finish write!")