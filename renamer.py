import os
import re

rename = []
path = '/Users/askopelevich/Music/iTunes/iTunes Media/Music'
os.chdir(path)
for fo in os.listdir(): #get list of artist folders
    if fo != '.DS_Store':
        print('Artist:')
        os.chdir(fo)
        print(os.getcwd())
        for al in os.listdir():  #for each artist folder, list of album folders
            if al != '.DS_Store':
                print('Album:')
                os.chdir(al)
                print(os.getcwd())
                for so in os.listdir(): #for each album, get names of files
                    if so != '.DS_Store':
                        print('Song')
                        print(so.encode('utf-8'))
                        if re.match(' - ', so): #add files w/ ' - ' to list to make sure it works
                            rename.append(so)
                            #rename files
                os.chdir('..')
        os.chdir('..')

for name in rename:
    print(name)
