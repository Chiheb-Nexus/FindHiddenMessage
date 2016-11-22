# FindHiddenMessage
Find and decode hidden messages in Bitcoin's blockchain explorer

# Some blocks with hidden messages
	 1- 0000000000000000011c72438a79cfa791122b4ba160ff124606a600a25d2b5f
	 2- 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
	 3- 0000000000000000011c72438a79cfa791122b4ba160ff124606a600a25d2b5f
	 
# Usage
Open the script file: `FindHiddenMsgBlockchain.py`
then 

```python
	# Change this line with your Bitcoin block hash
	block_hash = "PUT_YOUR_BLOCK_HASH_HERE"
	app = HexToString(block_hash)
```
Then launch the script

```bash
$ python3 FindHiddenMsgBlockchain.py
```
There will be an output file called `msg_raw_block` or your file's name if you changed it.
Open it with `nano` or `vi` and look into the ouput data in order to find any hidden message in the block hash used.
