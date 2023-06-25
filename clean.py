#!/usr/bin/python
import os
import sys
import shutil

def main(argv):
	if len(argv) > 1:
		tier = argv[1]
		if tier == "all":
			try:
				shutil.rmtree(f"Raw/")
			except:
				pass
			print(f"Deleted all raw files")
			return
		try:
			os.remove(f"Raw/{tier}")
		except:
			pass
		try:
			shutil.rmtree(f"Raw/moveset/{tier}")
		except:
			pass
		print(f"Deleted raw file and movesets for {tier}")
	else:
		print('Deleted nothing, specify a tier or "all" to delete all')


if __name__ == "__main__":
    main(sys.argv)