from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
import os, shutil

def copy_static_files(origin, destination):
  
  # If the path doesn't exist, create it
  if not os.path.exists(destination):
    print(f"Creating directory: {destination}")
    os.mkdir(destination)
  
  # check for an invalid folder name
  if not os.path.exists(origin):
    raise NameError("Invalid folder")

  files = os.listdir(origin)
  for file in files:
    path = os.path.join(origin, file)
    new_destination_path = os.path.join(destination, file)
    print(f"Copy {path} to {new_destination_path}")
    
    if os.path.isfile(path):
      print(f"We have a file {path}")
      shutil.copy(path, new_destination_path)
      print(f"Copied! {path}")
    
    else:
      print(f"This is not a file, {path}")
      if not os.path.exists(new_destination_path):
        os.mkdir(new_destination_path)
      copy_static_files(path, new_destination_path)
      
  print("Done copying files")



def main():
  origin = "static"
  destination = "public"
  result = copy_static_files(origin, destination)




main()
