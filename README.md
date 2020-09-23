# MScThesis
Source coding for processing SLA photographs.<br />
The script "SLA_automation.py" requires Python 3.8 to be installed on your machine. It is written specifically for the file naming and folder system that I used for my Masters thesis. However this can be easily altered inside the scripts for what you are looking for.<br />
The other script used for ImageJ version 1.52s that was integrated into the python script for a simple automation technique.<br />
The python modules were called in first then the directory containing the photographs was sourced.<br />
Using glob the specific file folder of "Photos/RW" was located for every subfolder inside the first sourced directory.<br />
The names of photos are then copied and shortened to get the plant ID that each photo was named for to create a string of all the photos to be analysed as "TODO".<br />
The photos were then opened one at a time in ImageJ and ran the second script "SLAprocess.ijim". This script puts a processing filter on the photo to remove any green then replace it with pink. Sharper lines around the leaf edges are then defined and the contrast is increased using "Threshold". The final photo is then pasted with the plant ID and suffixed with "processed.jpg" as a check to the user that the photo has been altered. <br />
Once done the python script will continue through the "TODO" string until it has no more left then end with a closing statement or simply none if no photos were differentially named from the ones given in the final processed directory.<br />

