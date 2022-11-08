from flask import Blueprint, render_template, redirect,request, jsonify
import datetime
import requests
import json
from flask import Flask, request, json, Response
from flask_cors import CORS

'''

'''
app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/hello',methods=['GET'])
def index():
	return jsonify("Hello World")


@app.route('/getcasebylist',methods=['GET'])
def mygetfile():
	if request.method == 'GET':
		print(request)
		caseID = request.args.get('cases','')
		key=request.args.get('key',None)
		sub=request.args.get('sub',None)
		
		file=open('caseR.txt','r')
		cases=json.load(file)
		file.close()
		
		if len(caseID)==0:
			Result=[]
			for candidate in cases[key][sub][:5]:
				candidate['frontendConstruction']=[]
				Result.append(candidate)
			res = {
				'retCode':200,
				'cases':Result
			}
			return jsonify(res)
		casesAim=caseID.split('~')
		Result=[]
		for ID in casesAim:
			for candidate in cases[key][sub]:
				if candidate['caseID']==int(ID):
					candidate['frontendConstruction']=[]
					Result.append(candidate)
		if len(Result)>5:
			Result=Result[:5]
		res = {
			'retCode':200,
			'cases':Result
		}
		return jsonify(res)


@app.route('/getfile',methods=['GET'])
def getfile():
	if request.method == 'GET':
		fileID = request.args.get('fileID',None)
		methodID = request.args.get('methodID',-1)
		file=open('files/'+str(fileID)+'txt','r')
		codes=file.readlines()
		file.close()
		methodcode=[]
		if methodID>=0:
			file=open('methods/'+str(methodID)+'txt','r')
			methodcode=file.readlines()
			file.close()
		res = {
			'retCode':200,
			'codes':codes,
			'methodcode':methodcode,
			'apis':[],
			'import':[]
		}
		return jsonify(res)

@app.route('/openfilebyid',methods=['GET'])
def opencase2():
	if request.method == 'GET':
		ID = request.args.get('fileID')
		cID=request.args.get('caseID')
		file=open('caseR.txt','r')
		cases=json.load(file)
		file.close()

		for key in list(cases.keys()):
			for sub in list(cases[key].keys()):
				for case in cases[key][sub]:
					if case['caseID']==int(cID):
						candidate=case
		
						
						f=open('files/'+str(ID)+'.txt','r',encoding='utf-8',errors='ignore')
						cs=f.readlines()
						f.close()

						codes=''
						for line in cs:
							if len(codes)==0:
								codes+=line
							else:
								codes+=''+line
						
						apis=[]
						for API in candidate['apis']:
							if API['ID']==ID:
								for mAPI in API['api']:
									for a in mAPI['api']:
										temp={}
										name=a.split(':')
										temp['label']=name[0]
										temp['children']=[]
										t=''
										for p in name[1:]:
											t+=p
											t+=' '
										temp['children'].append({'label':t})
										apis.append(temp)
							if len(apis)>0:
								break
						res = {
							'retCode':200,
							'codefile':codes,
							'apis':apis
						}
						return jsonify(res)
	
@app.route('/opencase',methods=['GET'])
def opencase():
	if request.method == 'GET':
		ID = request.args.get('caseID')
		file=open('caseR.txt','r')
		cases=json.load(file)
		file.close()

		for key in list(cases.keys()):
			for sub in list(cases[key].keys()):
				for case in cases[key][sub]:
					if case['caseID']==int(ID):
						candidate=case
		
						startfile=candidate['startFile']
						startMethod=candidate['startMethod']

						f=open('files/'+str(startfile)+'.txt','r',encoding='utf-8',errors='ignore')
						cs=f.readlines()
						f.close()

						m=open('methods/'+str(startMethod)+'.txt','r',encoding='utf-8',errors='ignore')
						ms=m.readlines()
						m.close()

						codes=''
						for line in cs:
							if len(codes)==0:
								codes+=line
							else:
								codes+=''+line
						piece=''
						for line in ms:
							if len(piece)==0:
								piece+=line
							else:
								piece+=''+line

						apis=[]
						for API in candidate['apis']:
							if API['ID']==startfile:
								for mAPI in API['api']:
									if mAPI['ID']==startMethod:
										for a in mAPI['api']:
											temp={}
											name=a.split(':')
											temp['label']=name[0]
											temp['children']=[]
											t=''
											for p in name[1:]:
												t+=p
												t+=' '
											temp['children'].append({'label':t})
											apis.append(temp)
										break
							if len(apis)>0:
								break
						res = {
							'retCode':200,
							'codefile':codes,
							'codepiece':piece,
							'dirs':candidate['frontendConstruction'],
							'apis':apis,
							'fullapi':candidate['apis']
						}
						return jsonify(res)
	   
 
if __name__ == '__main__':   
	
	app.run(host ='0.0.0.0',port = 5000)