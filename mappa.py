import math
import requests
import os

path =  os.getcwd()+"/imgs/"

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

def download(z):
	x = 0
	y = 0
	counter = 2**z - 1
	
	max_files = 2**z*2**z
	download_counter = 0
	while x <= counter:
		y = 0
		while y <= counter:
			f = os.path.exists(f"imgs/{z} {x} {y}.png")
			if f == False:
				try:
					tile_img_url = requests.get(f'https://tile.openstreetmap.org/{z}/{x}/{y}.png')
					if tile_img_url.status_code == 200  :
						print(f"donwloading {download_counter} from {max_files}")
						with open(f"imgs/{z} {x} {y}.png" , 'wb') as f:
							f.write(tile_img_url.content)
						print(f"done {download_counter+1} from {max_files}")
					else:
						print("connection is failed")
					y+=1
					download_counter+=1
				except:
					print(f"file {z} {x} {y} failed")	
			else:
				print(f'file is here {download_counter} from {max_files}')	
				download_counter+=1
				y+=1
		x+=1	
	
for i in range(1):
	download(i)		
