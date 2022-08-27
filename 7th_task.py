# import json
# with open('5th_task.json','r') as f:
#     a=json.load(f)
# dic={}
# i=0
# eng=0
# h=0
# t=0
# te=0
# while i<len(a):
#     if a[i]['director']==['Sundar C.']:
#         eng=eng+1
#         dic['Sundar C.']=eng
#     if  a[i]['director']==['Hrishikesh Mukherjee']:
#         h=h+1
#         dic['Hrishikesh Mukherjee']=h
    
#     if  a[i]['director']==['Mani Ratnam']:
#         t=t+1
#         dic['Mani Ratnam']=t
    
        
#     i=i+1
# with open('7th_task.json','w')as f:
#     json.dump(dic,f,indent=6)


import json
with open("5th_task.json","r") as f:
    a=json.load(f)
count={}
d1=[]
i=0
while i <len(a):
    if a[i]["director"]in count:
        count[a[i]["director"]]+=1
    else:
        count[a[i]["director"]]=1
    i=i+1
with open ("imdb 7_task.json","w") as k:
    json.dump(count,k,indent=2)
    
