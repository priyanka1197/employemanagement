import re
string=str({"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]})
#print("string is-->",string)
nums="0123456789"
i=0
whitelist=set('id:0123456789 code:0123456789')
answer=''.join(filter(whitelist.__contains__,str(string))).split(" ")
result=[]
#print("answer-->",answer)
for i in range(0,len(answer)-1):
    if(answer[i]=="id:" or answer[i]=="code:"):
        result.append(answer[i+1])

print(result)