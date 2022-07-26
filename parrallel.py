import random
from random import randrange, uniform, random
from datetime import timedelta, strptime
from datetime import datetime
import os
import sys
from ast import literal_eval

filePath = "C:/Users/samar/proj/a_file.txt" # Change to your full file path
fileDir = "C:/Users/samar/proj" # Change to your folder

#*************************************************************************************************************/
#***** Given a start and end time stamp this function generates random start timestamps for n video plays ****/
#*************************************************************************************************************/

def randomtimes(start, end, n):
    frmt = '%d-%m-%Y %H:%M:%S'
    stime = datetime.strptime(start, frmt)
    etime = datetime.strptime(end, frmt)
    td = etime - stime
    return [(random() * td + stime).replace(microsecond=0) for _ in range(n)]

#*************************************************************************************************************/
#***** Given start times this video adds duration to get end dates for n video plays                    ******/
#*************************************************************************************************************/
def simulateVideoPlays(playlist, start_times):
    for i in range(0, len(start_times)-1):
        VideoPlay = {
        'startTime' : '1/1/2008 1:30 PM',
        'endTime' : '1/1/2009 4:50 AM'
        }
        myVideoPlay = VideoPlay
        frmt = '%Y-%m-%d %H:%M:%S'
        random_second = randrange(120 * 60)
        x = start_times[i]
        datetimeobj=datetime.strptime(str(x),"%Y-%m-%d %H:%M:%S")
        myVideoPlay['startTime'] = str(x)
        myendtime = start_times[i] + timedelta(seconds=random_second)
        myVideoPlay['endTime'] = str(myendtime)
        frmt = '%Y-%m-%d %H:%M:%S'
        playlist.append(myVideoPlay)
        del myVideoPlay
    return playlist

#*************************************************************************************************************/
#***** We first get the start and end timestamp for the time during which videos will play.             ******/
#***** Then we ask for the maximum number of videos we would like played in the this timeframe and      ******/
#***** start and end at random times. This start and end timestamp data is saved in a file              ******/
#***** We first get the start and end timestamp for the time during which videos will play.             ******/
#***** Then we determine the number of seconds between our original start and end timestamp             ******/
#***** and for every one second period we printout the total numbr of videos playing in parrallel       ******/
#***** We only provide data for timestamps when a change in the total number of videos playing in       ******/
#***** parrallel occurs, so that redundant messages are not displayed.                                  ******/
#*************************************************************************************************************/
def main():
    option = True
    while option: 
        try:
            start_window = input("Please enter start timestamp in the form: yyyy-mm-dd hh:mm:ss OR q to quit ")
            if start_window == "q":
                option = False
                break
            else:
                date1_obj = datetime.strptime(start_window, "%Y-%m-%d %H:%M:%S")
        except:
            print("Not a Valid Timestamp")
            option = False
            break
        else:
            pass
    
        try:
            end_window = input("Please enter end timestamp in the form: yyyy-mm-dd hh:mm:ss ")
            date2_obj = datetime.strptime(end_window, "%Y-%m-%d %H:%M:%S")
        except:
            print("Not a Valid Timestamp")
            option = False
            break
        else:
            pass
        try:
            num_seconds = int(abs(date1_obj.timestamp() - date2_obj.timestamp()))
            assert num_seconds > 0
        except:
            print("End Timestamp must be greater than start timestamp")
            option = False
            break
        else:
            pass
        
        try:
            num_process = input("Please enter number of video plays to simulate between start and end timestamps")
            num_process = int(num_process)
            assert num_process > 0
        except:
            print("Number of Videos must be numeric")
            option = False
            break
        else:
            pass
        start_times = randomtimes('01-01-2022 00:00:00', '02-01-2022 00:00:00', num_process)
        playlist = []
        os.chdir(fileDir) 

        #add proc call here
        playlist = simulateVideoPlays(playlist, start_times)
        
        print("Simulating Video plays start and end times and saving to datafile...")
    
        try:
            textfile = open(filePath, "w")
            for element in playlist:
                textfile.write(str(element) + "\n")
        except:
            print("Error witing data file for simulation")
        finally:
            textfile.close()
        processList = []
        
        with open(filePath) as input_data:
            for line in input_data:
                VideoPlay = {
                'startTime' : '1/1/2008 1:30 PM',
                'endTime' : '1/1/2009 4:50 AM'
                }
                VideoPlay = literal_eval(line)
                processList.append(VideoPlay)
                del VideoPlay
        
        print("Reading Data File Completed")
        prev_count = -1
        for i in range(0, num_seconds):
            currentTime = date1_obj + timedelta(seconds=i)
            divs = [x for x in processList if datetime.strptime(str(x['startTime']),"%Y-%m-%d %H:%M:%S") <= currentTime and datetime.strptime(str(x['endTime']),"%Y-%m-%d %H:%M:%S") >= currentTime]
            if prev_count != len(divs):
                print("AT Time: "+ str(currentTime) + " : " + str(len(divs)) + " videos playing")
                prev_count = len(divs)
            del divs
        break

    


main()