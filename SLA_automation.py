# Automating File Analysis
import os # import os module
##import re # regexp
directory = "C:/Users/Jenn/Documents/Thesis/RILs Screening/"
os.chdir(directory) # need this to ensure photos are searched for properly
import glob
files = glob.glob(r'*/Photos/RW/*.JPG', recursive=False) # look for all RW photos
import subprocess # for opening other programs
import time # for delaying the open and processing


processed = glob.glob(r'*\SLA\Processed\*', recursive=False)
def remove_prefix_and_suffix(text, suffix):
    intermediate = os.path.basename(text)
    return intermediate.strip(suffix)
processed_raw = []
for i in range(0,len(processed)):
    processed_raw.append(remove_prefix_and_suffix(processed[i],"-(Colour_2)-processed.tif"))

files_raw = []
for i in range(0,len(files)):
    files_raw.append(remove_prefix_and_suffix(files[i],""))
                     
# check non-matching:
TODO = list(set(files_raw) - set(processed_raw)) #what is different in raw
#print(list(set(processed_raw) - set(files_raw)))
import fnmatch
def find(pattern, path):
    result = [] # so it only outputs one
    for root, dirs, files in os.walk(path): # find all the files I need
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

files = []
print("Getting file locations:")
#Remove up to RILs Screening

for i in range(0, len(TODO)):
    temp = find(TODO[i], path="C:\\Users\\Jenn\\Documents\\Thesis\\RILs Screening\\")
    files.append(os.path.relpath(temp[-1],"C:\\Users\\Jenn\\Documents\\Thesis\\RILs Screening\\")) # last one is always RW
    print(round(i/len(TODO)*100,0), "% done.") # progress

time.sleep(0.5)
print("There are", len(files), "files.")
if len(files) == 0:
    pass # list is empty
else:
    print("Finished compiling file locations.")
    files = sorted(files)
    print(files)
    print("Processing following files now.")
    subprocess.Popen(['C:\Program Files\ImageJ\ImageJ.exe'])

# Now give me photos
for i in range(0,len(files)): # for test start with the last 2 len(files)-1
    subprocess.Popen(["C:\Program Files\ImageJ\ImageJ.exe",files[i]]) # static placement of
    time.sleep(2)
    subprocess.Popen(["C:\Program Files\ImageJ\ImageJ.exe",
                     "C:\Program Files\ImageJ\macros\SLAprocess.ijm"]) # open macro to prompt editing
    time.sleep(4) ## pause to let the program finish
    print("Finished processing", files[i])

print("All done now, thank you :)")
