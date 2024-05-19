# Import module
import os

# Assign directory
directory = r"C:\Users\Lenovo\Downloads\gfg-test"

# Iterate over files in directory
for path, folders, files in os.walk(directory):
	# Open file
	for filename in files:
		with open(os.path.join(directory, filename)) as f:
			print(f"Content of '{filename}'")
			# Read content of file
			print(f.read())
		print()

	# List contain of folder
	for folder_name in folders:
		print(f"Content of '{folder_name}'")
		# List content from folder
		print(os.listdir(f"{path}/{folder_name}"))
		print()

	break
