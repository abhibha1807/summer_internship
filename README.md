# Detecting Geo-spatialness of prepositions
This repo provides the code related to my journal work. It has the Geo Parser, the classifier code and the transfer learning code. 

## Geo Parser:
The Geo Parser performs a lookup from 4 gazetters (Open Street Map, Ordanance Survey, GeoText, Geonames) to detect the occurence of a geographic featuretype or a placename from some text. It uses API calls and string matching to detect occurences of the above mentioned entities. The module is different from other placename detection tools in the aspect that it also detects geographic feature types. I have used ADL feature types dictionary for this. 

## ML Code:
The code folders contains all the code used to perform my task. 
