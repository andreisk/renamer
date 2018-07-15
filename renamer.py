import os
import re

os.chdir(path)
for fo in os.listdir(): #get list of artist folders
    if fo != '.DS_Store':
        os.chdir(fo)
        for al in os.listdir():  #for each artist folder, list of album folders
            if al != '.DS_Store':
                os.chdir(al)
                for so in os.listdir(): #for each album, get names of files
                        ma = re.match('.*? - (.*)', so)
                        if ma: #add files w/ ' - ' to list to make sure it works
                            os.rename(so, ma.group(1)) #rename files
                os.chdir('..')
        os.chdir('..')
