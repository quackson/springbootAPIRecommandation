import json

file=open('APIList.txt','r')
apis=json.load(file)
file.close()

R=[]
for api in list(apis.keys()):
	temp=api.split(':')
	package=temp[0]
	class_=temp[1]
	method=temp[2]
	cases=apis[api]
	R.append({
		'package':package,
		'class':class_,
		'api':method,
		'cases':cases
		})

file=open('APIList2.txt','w')
file.write(json.dumps(R))
file.close()