import os
rename = []
os.chdir('/Users/askopelevich/Music/iTunes/iTunes Media/Music')
for fo in os.listdir(): #get list of artist folders
    print(fo)
#for each artist folder, list of album folders
#for each album, get names of files, add files w/ ' - ' to list
