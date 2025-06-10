import importlib
import os
import argparse

def find_mod_path(mod_name, classify_file=False):
	"""
	Prints file location of a given module 
	and classifies its type if requested.
	"""

	print(f"\n------------ Module: {mod_name} ------------")
	try:
		module = importlib.import_module(mod_name)
	
	# Handle case where module doesn't exist
	except ModuleNotFoundError:
		print(f"Module '{mod_name}' not found\n")
		return
      
	# Catch any other import-related errors
	except Exception as e:
		print(f"Error importing module '{mod_name}': {e}\n")
		return

	if hasattr(module, "__file__") and module.__file__:
		print(f"Module '{mod_name}' is located at:\n{module.__file__}\n")
	else:
		# Built-in modules will not have a __file__
		print(f"Module '{mod_name}' is built-in (no file path, human-readable code online)\n")
		return
    
	if classify_file:
		path = module.__file__
		if os.path.basename(path) == "__init__.py":
			print(f"{mod_name} is a package (directory with __init__.py).\n")
		
        # .pyd is essentially the Windows version of .so
		elif path.endswith(('.so', '.pyd')):
			print(f"{mod_name} is a C extension module, human-readable code online.\n")
			
		elif path.endswith(".py"):
			print(f"{mod_name} is a pure python module (.py file)\n")
			
		else:
			print(f"{mod_name} type not classified by this program (yet).\n")


def find_mod_paths(mod_names, classify_file=False):
	"""
	Loop over a list of module names and print 
	their file locations and classifications.
	"""
	for mod_name in mod_names:
		find_mod_path(mod_name, classify_file=classify_file)

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Finds the file path of a \
										python module or package.")

	# Accept one or more module names to look up
	parser.add_argument("mod_names", nargs = "+", help="Name of the module to inspect")

	# Optional flag to include classification details
	parser.add_argument("--details", action="store_true", 
					    dest="classify_file", help="Show extra info about modules")
	
	args = parser.parse_args()
	find_mod_paths(args.mod_names, args.classify_file)
	
