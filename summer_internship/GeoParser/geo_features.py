import sys
import re
import test_stanford
from nltk.stem.porter import *

# def check_inlist(arg):
# 	arg=arg+'\n'
# 	with open('geonouns-old.txt','r') as f:
# 		for word in f:
# 			# print(word)
# 			if arg == word:
# 				return True
# 	return False

def geo_features(s):
	final_l=[]
	with open('geonouns-old.txt','r') as f:
		for word in f:
			word=word.strip()
			final_l.append(word)


# def geo_features(s):
# 	final_l=[]
# 	with open('ADL_featureTypes_edited.txt','r') as f:
# 		for strg in f:
# 		# strg=f.readline()
# 			if strg == '\n':
# 				continue
# 			else:
# 				strg=strg.replace("\"","")
# 				l=[]
# 				l=strg.split(';')
# 				final_l.append(l[1])
	
	c=0
	r=[]
	split_s=s.split(' ')
	print('SPLITTTTTTTTT_SSSSSSSSSSSSS',split_s)
	split_s[len(split_s)-1]=split_s[len(split_s)-1].replace('\"\n',"")
	for i in final_l:
		print('ping:',i)
		if i in s:
			print('I:',i)
			split_i=i.split(' ')

			set_s=set()
			set_i=set()
			for l in split_s:
				set_s.add(l)
			print('SET_SSSSSSSSSSSS:',set_s)
			for k in split_i:
				set_i.add(k)
			print('SET_IIIIIIIIIIII:',set_i)
			
			if set_i.issubset(set_s):
				print('HEYYYYYYYYYYYYY',i)
				r.append(i)
				c=c+1
				for j in split_i:
					# s=re.sub(j,"",s,count=1)
					s=s.replace(j,"",1)
			print('SSSSSSSSSSSSSS:',s)
		cnt=0
		for i in r:
			cnt=cnt+s.count(i)
			if s.count(i)>0:
				r.append(i)
				f=i.split(' ')
				for j in f:
					s=s.replace(j,"",1)
		print('\n')
		print('CNTTTTTTTTTT',cnt)
		print('\n')
		
		return (s,c+cnt,r)
	


# 	r=[]
# 	c=0
# 	split_s=s.split(' ')
# 	print('SPLITTTTTTTTT_SSSSSSSSSSSSS',split_s)
# 	split_s[len(split_s)-1]=split_s[len(split_s)-1].replace('\"\n',"")

# 	for i in final_l:
# 		if i in s:
# 			print('I:',i)
# 			split_i=i.split(' ')

# 			set_s=set()
# 			set_i=set()
# 			for l in split_s:
# 				set_s.add(l)
# 			print('SET_SSSSSSSSSSSS:',set_s)
# 			for k in split_i:
# 				set_i.add(k)
# 			print('SET_IIIIIIIIIIII:',set_i)
			
# 			if set_i.issubset(set_s):
# 				print('HEYYYYYYYYYYYYY',i)
# 				r.append(i)
# 				c=c+1
# 				for j in split_i:
# 					# s=re.sub(j,"",s,count=1)
# 					s=s.replace(j,"",1)
# 			print('SSSSSSSSSSSSSS:',s)

# 	cnt=0
# 	for i in r:
# 		cnt=cnt+s.count(i)
# 		if s.count(i)>0:
# 			r.append(i)
# 			f=i.split(' ')
# 			for j in f:
# 				# s=re.sub(j,"",s,count=1)
# 				s=s.replace(j,"",1)
# 	print('\n')
# 	print('CNTTTTTTTTTT',cnt+c)
# 	print('\n')
	
# 	return (s,c+cnt,r)
	
	
# geo_features('The barn')



