import subprocess

subprocess.run(["git", "add", "."]) 
subprocess.run(["git", "commit" , "-m", "\"updated notes\""])
subprocess.run(["git", "push"])