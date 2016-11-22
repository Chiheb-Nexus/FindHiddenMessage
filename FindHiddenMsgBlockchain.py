#!/usr/bin/python

#
# Retrive Bitcoin raw blocks and decode it in order to find hidden messages
# Script author: Chiheb Nexus
#

from json import loads
from urllib.request import Request, urlopen

class HexToString:
	def __init__(self, block_hash):		
		self.run(block_hash)
		
	def run(self, block_hash = ""):
		n = 70 # Split the decoded output every 70 characters for better visualisation of the output file
		data = self.get_raw_block(block_hash)
		ascii_data = self.return_ascii_from_hex(data["rawblock"])
		ascii_splited = [ascii_data[i:i+n] for i in range(0, len(ascii_data), n)]
		
		try:
			with open("msg_raw_block", 'a') as output: # msg_raw_block is the name of the output file
				for splited in ascii_splited:		   # change it whaterver you want or keep it :-)	
					output.write(splited + "\n")
				
			print("Done") # Job ends here 
		except Exception as e:
			print("Error occurred wile opening/writing into the file\n", e)
		
	def get_raw_block(self, block_hash = ""):
		# We'll use blockexplorer.com as Bitcoin explorer for our requests 
		# in order to retrieve bitcoin's raw blocks
		url = "https://blockexplorer.com/api/rawblock/"
		print("Fetching data...") # Job begins here
		try:
			# Use your favorite User Agent
			request = Request(url + block_hash, headers= {'User-Agent' :\
				"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36"})
			response = urlopen(request)
			data = loads(response.read().decode("utf8"))
			return data
		except Exception as e:
			print("Cannot fetch explorer's URL\n", e)
			return ""
		
	def return_ascii_from_hex(self, hex_string = ""):
		try:
			# decode from hex to ascii
			return ''.join(chr(int(hex_string[i:i+2], 16)) for i in range(0, len(hex_string), 2))
		except Exception as e:
			print("Cannot decode the input string\n", e)
			return ""
			
# Run the script
if __name__ == '__main__':
	# Some blocks with hidden messages
	# 1- 0000000000000000011c72438a79cfa791122b4ba160ff124606a600a25d2b5f
	# 2- 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
	# 3- 0000000000000000011c72438a79cfa791122b4ba160ff124606a600a25d2b5f
	
	# Change this line with your Bitcoin block hash
	block_hash = "0000000000000000011c72438a79cfa791122b4ba160ff124606a600a25d2b5f"
	app = HexToString(block_hash)
	
