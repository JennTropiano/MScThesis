# MScThesis
Source coding for processing SLA photographs.<br />
The script "SLA_automation.py" requires Python 3.8 to be installed on your machine. It is written specifically for the file and folder system that I used for my Masters thesis.<br />
The other script used for ImageJ was integrated into the python script for a simple automation technique.
The python modules were called in first then the directory containing the photographs was sourced.
Using "glob" the specific file folder of "Photos/RW" was located for every subfolder inside the first sourced directory.
Once inside the names of the photos were clipped for just the ID that each photo was named for a string of all the photos to be analysed as "TODO".
The photos were then opened one at a time and ran the second script "SLAprocess.ijim". This script puts a processor overtop of the photo to remove any green then replace it with pink. Sharper lines around the leaf edges are then defined and the contrast is increased using "Threshold". The final photo is then pasted with the plant ID and suffixed with "processed.jpg" as a check to the user that the photo has been altered. 
Once done the python script will end with a closing statement or simply none if no photos were different from the ones given in the final processed directory.

