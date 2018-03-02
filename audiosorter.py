#!/usr/bin/python3

import os
import sys
import shutil
from pytag import Audio   

if(len(sys.argv) == 1):
	dirlist = os.listdir(os.getcwd())
elif(len(sys.argv) == 2):
	dirlist = os.listdir(sys.argv[1])
else:
	print("Expected one argument or fewer")
	sys.exit()


count = 0

for song in dirlist:
	
	if(song[-4:] != ".mp3"):
		continue
			
	try:
		audio = Audio(os.getcwd()+'/'+song)
	except:
		continue

	if(not(audio.artist is None)):
		count += 1
		
		artist = str(audio.artist).strip('\0')
		title = str(audio.title).strip('\0')

		if(os.path.isdir(str(os.getcwd()+'/'+artist))):
			shutil.move(str(os.getcwd()+'/'+song),os.getcwd()+'/'+artist)
		else:
			os.mkdir(artist)
			shutil.move(str(os.getcwd()+'/'+song),os.getcwd()+'/'+artist)
			print("Created directory: "+artist)
		
		if((title is not None) and not(title == '') and not(title == 'Unknown') and not(title == "None")):
			os.chdir(artist)
			if(not(os.path.exists(os.getcwd()+'/'+str(title + ".mp3")))):
				os.rename(song,title+".mp3")
				print("Renamed song: " + song + " to " + title+".mp3")
			else:
				i = 1
				while((os.path.exists(str(title + ' (' + str(i) + ')' + ".mp3")))):
					i += 1			
				os.rename(song,title+" ("+str(i)+").mp3")
				print("Renamed song: " + song + " to " + title+".mp3")

			os.chdir("..")	

if(count > 0):
	print("Sorting completed. " + str(count) + " mp3 files were sorted")
else:
	print("No unsorted mp3 files found")
