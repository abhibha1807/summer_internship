# from nltk.tag import StanfordNERTagger

# # def test_stanford_ner(sentence):
# st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz',)

# print(st.tag("Rio de Janeiro is in Brazil"))


# import os
# import subprocess
# import xml.etree.ElementTree as ET
# import re


# def test_stanford_ner():
    
#     return(subprocess.run(
#         'java -mx600m -cp "*:lib/*" edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier /Users/abhibhagupta/Downloads/stanford-ner-2018-10-16/classifiers/english.all.3class.distsim.crf.ser.gz -textFile input.txt -outputFormat inlineXML 2>parse.out' ,
#         shell=True,     # execute with shell
#         check=True, stdout=subprocess.PIPE     # error check
#     ).stdout.decode('utf-8'))

from nltk.parse import CoreNLPParser
def test_stanford_ner(s):
    ner_tagger = CoreNLPParser(url='http://localhost:9000', tagtype='ner')
    return(list(ner_tagger.tag((s.split()))))

