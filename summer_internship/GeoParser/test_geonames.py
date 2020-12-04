import json
import requests
import sys

def test_geonames(location):
	base_url="http://api.geonames.org/searchJSON?q="
	query=location
	url=base_url+query+"&maxRows=10&username=abhibha1807"
	response = requests.get(url)
	temp_l=[]
	# print(response.status_code)
	# print(url)
	todos = json.loads(response.text)
	items=todos.items()
	# print(items)
	for i,j in items:
		if i=="geonames":
			if len(j)!=0:
				for k in j:
					d=k.items()
					for l,m in d:
						
						if l=="toponymName":
							# print(m,"--------------------------------")
							y=m.split(' ')
							x=location.split(' ')
							print('------------',x,y)
							# if (y)==(x):
							for p in y:
								
								for q in x:
									
									if p==q:
										print('ppppppppppp:',p,q)
										temp_l.append(d)	
								# print(d)
								# temp_l.append(d)
							# s=''
							# for q in y:
							# 	s=s+q[0].upper()
							# 	print(s)
							# 	for a in s:
							# 		if a == 
							# 		print(d)
							# 		temp_l.append(d)

						# print(l)
								# print('\n')
				# print('success!!'+location)
				# return True
			# else:
				# print('nothing to show!'+location)
				# return False
		# else:
		# 	print(i,j)

	if len(temp_l)==0:
		return False
	else:
		return True

# test_geonames('Mumbai')
