# import urllib
# import urllib.request as urllib2 
# import sys
# from urllib.request import Request, urlopen

# req = Request('https://geocoder.tilehosting.com/q/zurich.js?key=zjHdrAD8A6tMYePMBF2t')
# # values = {'key':'zjHdrAD8A6tMYePMBF2t'}
# # data=urllib.parse.urlencode(values)
# # full_url=url+'?'+data
# # print(full_url)
# f = urlopen(req)
# print('success')
# response=f.read().decode('UTF-8')
# for line in response.
# splitlines():
# 	print(line) 
# print('-'*80)              
# f.close()

# # zurich.js?key=zjHdrAD8A6tMYePMBF2t
import json
import requests
import sys

def test_osm(location):
	base_url="https://geocoder.tilehosting.com/q/";
	key='zjHdrAD8A6tMYePMBF2t'
	# place=sys.argv[1]
	place=location
	url=base_url+place+'.js?key='+key
	response = requests.get(url)
	# print(response.status_code)
	print(url)
	temp_l=[]
	todos = json.loads(response.text)
	items=todos.items()
	for i,j in items:
		if i=="results":
			if len(j)!=0:
				for k in j:
					d=k.items()
					for l,m in d:
						if l=="display_name":
							x=location.split(' ')
							y=m.split(' ')
							# if y==x:
							for p in y:
								for q in x:
									if p==q:
										print('ppppppppppp:',p,q)
										temp_l.append(d)
								# print(d)
								#temp_l.append(d)


						# print(l)
								# print('\n')
	if len(temp_l)==0:
		return False
	else:
		return True
			# 	return True
			# else:
			# 	return False


		# else:
		# 	print(i,j)

	


# if type(l).__name__=='tuple':
						# 	for i in range(len(l)):
						# 		if l[i]=="alternative_names":
						# 			i=i+1
						# 			if l[i]==location:
						# 				return True;



						# if l[0]=="alternative_names":
						# 	if l[1]==place:
						# 		print(l[1])
						# 		return True


# if __name__ == '__main__':
# 	  main()
