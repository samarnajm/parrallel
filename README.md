# parrallel
parrallel videos project

Python Version: Python 3.9.1 [MSC v.1927 64 bit (AMD64)] on win32

List of imports:

import random
from random import randrange, uniform, random
from datetime import timedelta, strptime
from datetime import datetime
import os
import sys
from ast import literal_eval

Changes Needed to run code:

filePath = "C:/Users/samar/proj/a_file.txt" # Change to your full file path - This is the filename of the data file that the program will save and the full path to file
fileDir = "C:/Users/samar/proj" # Change to your folder - This is the folder the program uses to save data and read data from

How the program works:

We first get the start and end timestamp for the time during which videos will play.          
Then we ask for the maximum number of videos we would like played in the this timeframe and      
start and end at random times. This start and end timestamp data is saved in a file              
We first get the start and end timestamp for the time during which videos will play.             
Then we determine the number of seconds between our original start and end timestamp            
and for every one second period we printout the total numbr of videos playing in parrallel       
We only provide data for timestamps when a change in the total number of videos playing in       
parrallel occurs, so that redundant messages are not displayed. 

Sample data file created by program for a single run is attached with the code.

The output of this particular file is also attached. 
