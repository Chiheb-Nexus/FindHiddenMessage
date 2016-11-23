#!/usr/bin/python

#
# Retrive Bitcoin raw blocks and decode it in order to find hidden messages
# Script author: Chiheb Nexus
#

from json import loads
from urllib.request import Request, urlopen
from sys import exit
import argparse

class FindHiddenMsgBlockchain:
	def __init__(self):	
		url_raw = "http://btc.blockr.io/api/v1/block/raw/"
		parser = argparse.ArgumentParser(description = """
		This script can decode hidden messages in Bitcoin's block raw transactions
		""")
		parser.add_argument('-s', '--start', help = "First index of Bitcoin's block range", required = True, default = "1")
		parser.add_argument('-f', '--final', help = "Last index of Bitcoin's block range", required = True, default = "2")
		number = parser.parse_args()
		
		try:
			self.run(url = url_raw, start = number.start , stop = number.final)
			
		except ValueError:
			print("Error has occurred")
			print("Please enter a valid integers for Start and Final arguments.")
			exit(1)
		
	def run(self, url = "", start = "", stop = ""):
		try:
			for number in range(int(start), int(stop)+1):
				data = self.get_block_hash(url = url, block_number = str(number))
				
				print("[+] Fetching data for block: \t{0}".format(data["data"]["hash"]))
				self.run_output(block_hash = data["data"]["hash"], file_name = str(number))
				print("-> Data fetched.")
				
		except KeyboardInterrupt:
			user_data = input("\rDo you want to exit the program ? [Y/N]: ") 
			if user_data == "y" or "Y":
				exit(1)
			else:
				pass		
		
	def get_block_hash (self, url = "", block_number = ""):
		return self.get_raw_block(url = url, block_hash = block_number)
		
	def run_output(self, block_hash = "", file_name = ""):
		url_explorer = "https://blockexplorer.com/api/rawblock/"
		n = 70 # Split the decoded output every 70 characters for better visualisation of the output file
		
		data = self.get_raw_block(url = url_explorer, block_hash = block_hash)
		ascii_data = self.return_ascii_from_hex(data["rawblock"])
		ascii_splited = [ascii_data[i:i+n] for i in range(0, len(ascii_data), n)]
		
		try:
			with open(file_name, 'a') as output: # msg_raw_block is the name of the output file
				for splited in ascii_splited:		   # change it whaterver you want or keep it :-)	
					output.write(splited + "\n")
				
		except Exception as e:
			print("Error occurred wile opening/writing into the file\n", e)
		
	def get_raw_block(self, url = "",  block_hash = ""):
		# We'll use blockexplorer.com as Bitcoin explorer for our requests 
		# in order to retrieve bitcoin's raw blocks
		
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
	app = FindHiddenMsgBlockchain()
	
