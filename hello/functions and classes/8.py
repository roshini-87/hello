import json
data='''[
{
"id":1,
"name":"name1",
"color":[
"red",
"green"
]
},
{
"id":2,
"name":"name2",
"color":[
"pink",
"yellow"
]
}
]'''
m = json.loads(data)
name=[i['name']for i in m]
 
print(name)