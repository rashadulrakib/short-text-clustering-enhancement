import re

##read labels obtained from external clustering algorithm
def readClustLabel(fileName):
 file1=open(fileName,"r")
 lines = file1.readlines()
 file1.close()
 clustlabels = []
 for line in lines:
  line = line.strip()
  arr = re.split(",", line) 
  clustlabels = clustlabels + arr

 print("total labels from "+ fileName+" is "+ str(len(clustlabels)))
 return clustlabels
