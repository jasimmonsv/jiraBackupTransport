#! /usr/bin/python
#Python Version 2.7
#
#This script will tar the twice daily Jira backups for the week, copy them to a 
#defined folder for off site backup, and then move the just copied files into a 
#holding folder for deletion

import sys
import os
from os.path import isfile, join
import tarfile
import datetime
import shutil

startPath = '/var/atlassian/application-data/jira/export'
endFolder = 'hold'
transportFolder = '/home/jsimmons'

onlyfiles = [f for f in os.listdir(startPath) if isfile(join(startPath,f))]
if not os.path.isdir(join(startPath,'hold')): os.mkdir(join(startPath,endFolder))

#tar and gzip the files
weekNum= (datetime.datetime.now().day - 1) // 7+1
tarName = str(datetime.datetime.now().year)+'week'+str(weekNum)+'.tar.gz'
tar = tarfile.open(join(startPath,tarName),"w:gz")
for x in onlyfiles:
  tar.add(join(startPath,x))
tar.close()

#move the files into the holding folder
for x in onlyfiles:
  shutil.move(join(startPath,x),join(startPath,endFolder))

#move the tar file into the tranport folder for offsite transfer
shutil.move(join(startPath,tarName),transportFolder)
quit()
