# FindHiddenMessage
Find and decode hidden messages in Bitcoin's blockchain explorer

# Some blocks with hidden messages
	 1- Block: 437770
	 2- Block: 436928
	 3- Block: 433931
	 
# Usage
Decode messages of Bitcoin block ranges between 1 and 20

```bash
$ python3 FindHiddenMsgBlockchain.py -s 1 -f 20 -r n
```
If nothing was wrong, you'll have 20 new files in each one of them the decoded message hidden in the blocks.

**NB**: You can use :

	1- `-r y` to filter the output and have only human readable characters
	2- `-r n` to have the converted output without modifying it
	
Have fun!


