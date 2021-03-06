'''MIT License

Copyright (c) 2020 Vinicius Krieger Granemann

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

import time
import datetime
import sys
import os
'''import pyglet

song = pyglet.resource.media('thesong.mp3')
song.play()
pyglet.app.run()'''
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

mixer.init()
mixer.music.load(os.path.join(sys.path[0], 'thesong.ogg'))
mixer.music.play(-1)

clear = lambda: os.system('cls')

myInput = None

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# write a formatted version of time
def WriteFormattedTime():
    formattedTime = datetime.timedelta( seconds=(int(time.time() - startTime)) )
    return str(formattedTime)
def WriteCurrentFormattedTime():
    formattedTime = datetime.timedelta( seconds=(int(time.time() - startSessionTime)) )
    return str(formattedTime)
	

# store time data
def WriteToFile():
    with open(os.path.join(sys.path[0], myInput + ".xml"), "r+") as f:
        f.seek(0)
        f.write(str(time.time() - startTime))

clearScreen()
sys.stdout.write("""

                                       .***,,*,*,**,,,,,,,*********************************************/((/***,,*((*.                       
                                         ...........,***************************(//*#*******/************,*#,,*,***,*,,.                    
                                            .....,*********************/*////////////*///////*/*/*/*//***/***,*,,,,,,,/#*.                  
                                             .*****************//////*//////////////////////////////////*/**//####//#/(*/.,                 
                                           ,****************////////////////////////////////////////**((**//**///(**(//#*.(.                
                                        .,************/***///////////////////*%%/**////////////////////#**(*//////*//%//(*#(                
                                      .,************//**%(///////////////////*#(***%%//////////////////***%////////%##*/(%*/.               
                                    .(***************(#(///////////////////////****#%///////////////////////////////##**#%*/(               
                                   .,***************(*///////////////////////////////////////////////////////////////#(#%/*/(               
                                  .******************/////////////////////////////////////////////////////////////////##//*##               
                                 .*****************/*/////////////////////////////////////////////////%&(((////////////(#(/(,/              
                                 ****************/%,*/&%*///////////////////(//////////////////////////#((&#/////////////#*//#/             
                                ,***************,***,/&/*//////////////////(((@/*(&//(////////////////////////////////*//*(***/             
                                *****************//,,***/////////////(///(/((/&(//&&/(((///////////////////////////////(//**,**             
                                ********************/////////////////////(/(/(////////(//(////////////////////////////******,,,             
                               .****/***************//////////////////((((//(/(////(//////////////////(&*,////////////*///(*/*.             
                               .,******************///////////////////(///(((//(//(/(/(//////////////*%(**#(///////////*////(/              
                               .,*****************//////////////(/////(///////////(//((((/((///////////***@*/////////////**/**              
                               .,,****************///*///////////////////////////////////////(//(////////////////////******/*,              
                               .,**,,************//***/****/*////////////*#@@@,,&&#///////////////////////////////////****/*,               
                               .,*,,****,,,**//(#####%%%%%%&%&&&&%&%&&&&&%%%(/*,,,,,*(//(////////////////////////////*/****,                
                                **,,,,*////((((####%%%%%%%%%&&&&&&%%&%&&&&&&&&&&@@@@@@&&%%(/***//////(///////////////*(#***.                
                                ,,,,/////*,.,,..**//(###%%%%%&&&%%%%%%%%%%&%%%&%%%%##((//((((#####/**(##%%*//////////****/*                 
                                ,,,///*........ .      .,,//#%%%%%%%%%%%%#(/**,,,.,,..,,**,,,,,,*/(###(*(#(//////////*//*/*,                
                                .,*//*******///////****,,,**/(###%%%%%%####(//*///(((((##%%####((/**/(##((*****//////**/****                
                                 *//********,,*,....,*(/*,****/((#%%%%%%%%#((((/******,*(///*/((((((####(#((/**///**(/*/***,                
                                  /**//****, ./#%**..***(/#/,,*/(#%%&&&%%#(//*//*/%#*,.&.,,,.,////((((#((((((///**//*/****,.                
                                  */*///***,,*/(##(**/%@%#(//*,*/##%&&%%%#(/(/(#(#&&%/***(#(/////////(((((((((///*.,******,                 
                                  ,/*/////****///////((###((/***(##%&&%%%#((((////((((#(#%%##((((#((((((((((/////*...******                 
                                  .***///////**/////////(((///*/(#%%&%%%%%####((//////////((((######((((((((/////**#(. ,***                 
                                  .***///((((/(((((((((((((////(##%%%%%%%%%%%%%%###(###################((((//////**%%/((**.                 
                                  .***//(((######(#(##(#((/////(#%%%%%%%%%%%%%%%%%%%%#####%#%%%%%%%#####(((//////*/%((#%#/                  
                                  ,**///(((############(((/////(#%%&%%%%%%%%%%%%%%%&%%%%%%%%%%%%%%%%####(((//////*/#(%%%##                  
                                  ,***////(((##########((/////(#%%%%%%%%%###%%%%%&&&%%%%%%%%%%%%%%%#%##(((//////**/######/                  
                                  ,***////((((#(######((/////((%%%%&%%%%########%%%%%%%%%%%%%%&%%%%%##((((//////**(####(,                   
                                  .******///(((((##((((/(((((##%&&&&&%%%%%%%%%%##%%%%####%%%%%%%%%####((((/(////**//**/*,                   
                                   ,****/////(((((((((//((//(#%%&&&&&&%%%##(#####%%%%%%##((((#########((/(//////**(////*,                   
                                    ,*****////(((((((///*,.,*/#%%%%%%%#(((#(//(#%%%%%%%%######//((((((((((((///***/(////*                   
                                    .,*****////((((((((((/***,,///((((#########%%%##########(#((//((((((((((/****/(/////*                   
                                     ,*******/////(((((((((//////((###%################(#((((((((/(((((((((//****//////**,                  
                                      ,*******////((((((/((((((((####(########%#%#%%%##((///(/(((((/((((((//*****/////****.                 
                                      .,*********////(((##((###########%%#####((((//*,,/((((((((((/(((((///******/////*****,                
                                       .,*********/////(((((((////*///////////**/((/((#((((((((/(//((/////******/////******,,,.             
                                        .,,*,,,,*****,...,,,,,,*******/(((#((#(((((((##(((((((////////*/*******/////**********,,,,.         
                                          ,,,,,,,,********///(((#%##%###&%###(((((((##((/(////////*/*********/(////*****************,,      
                                           .,,,,,,,,**////**////(((((#(((((((((((((##((((/(//////*/********/((((//**********************,.  
                                             ..,,,,,*****//**********/*//*//((((##((((////////////*******((#(((//***********//////////*/***,
                                                .,,,,,*****/////**,,,,,,*//(((###((//////////*/*******//((#((((/*/////***//////////////////*
                                                  .,,,,,***///////,,,*//(((##((#(((//(///*///*******//(((#((((/*//////*/////////////////////
                                                   .,,,,****/////*///((##(#(#(((((////////********/////((#((///(((//////////////////////////
                                                    ,,,,*******/**////((((((/(((((//(///********//////((((////((((((////////////////////////
                                                     .,,,,********,,,*/*(///////(/////**********/////////////(((((((////////////////////////
                                                     ,,,,,,*,,,,*,,,,,***/*/////*/************////////*/////((((((((////////////////////////
                                                   ..,,,,,,..,.......,,*********************///////*/#(/////((((##((////**////////////(((((/
                                                ...,,,,,,,,,,,.........,,,,,,,,,,*,*********/*/*/**%&/*/////(((###(//*****///////////(((((((
                                              ...,,,,,,,,,,,,,,,,,.....,,,,,,,,,*****************%&**///////((#((((//******////////((((((((


       __ _                   _                _ _               
      /__(_) ___ __ _ _ __ __| | ___     /\/\ (_) | ___  ___     
     / \// |/ __/ _` | '__/ _` |/ _ \   /    \| | |/ _ \/ __|    
    / _  \ | (_| (_| | | | (_| | (_) | / /\/\ \ | | (_) \__ \    
    \/ \_/_|\___\__,_|_|  \__,_|\___/  \/    \/_|_|\___/|___/    
                                                                                                                                             
                     __ __________          _   _____  __                
             /\ /\  / //__   \_   \/\/\    /_\ /__   \/__\               
            / / \ \/ /   / /\// /\/    \  //_\\  / /\/_\                 
            \ \_/ / /___/ //\/ /_/ /\/\ \/  _  \/ / //__                 
             \___/\____/\/ \____/\/    \/\_/ \_/\/  \__/                 
                                                                                                                     
                         _____ _                  _____                _             
                        /__   (_)_ __ ___   ___  /__   \_ __ __ _  ___| | _____ _ __ 
                          / /\/ | '_ ` _ \ / _ \   / /\/ '__/ _` |/ __| |/ / _ \ '__|
                         / /  | | | | | | |  __/  / /  | | | (_| | (__|   <  __/ |   
                         \/   |_|_| |_| |_|\___|  \/   |_|  \__,_|\___|_|\_\___|_|   
                                                                                                         
                                By Hermitao


""")

projects = None
projectsFileContents = None

try:
    with open(os.path.join(sys.path[0], "Projects.xml"), "r+") as projectsFile:
        projectsFileContents = projectsFile.readlines()
except IOError:
    with open(os.path.join(sys.path[0], "Projects.xml"), "w+") as projectsFile:
        projectsFileContents = projectsFile.readlines()

        
projects = [x.strip() for x in projectsFileContents]

print("What project do you want to work on?\n")
for x in range( len(projects) ):
     print (projects[x])
myInput = input("\n")

startTime = time.time()
startSessionTime = time.time()

f = None
contents = None

if ((myInput + "\n") not in projectsFileContents):
    projects.append(myInput)
    with open(os.path.join(sys.path[0], "Projects.xml"), "a") as projectsFile:
        projectsFile.write(myInput + "\n")

# read or create file for elapsed time storage
try:
    with open(os.path.join(sys.path[0], myInput + ".xml"), "r+") as f:
        contents = f.read()
except IOError:
    with open(os.path.join(sys.path[0], myInput + ".xml"), "w+") as f:
        contents = f.read()

'''try:
    with open("Elapsed Time.xml", "r+") as f:
        contents = f.read()
except FileNotFoundError:
    with open("Elapsed Time.xml", "w+") as f:
        contents = f.read()'''

if (contents != ""):
    startTime = time.time() - float(contents)

while True:
    WriteToFile()
    sys.stdout.write("\r%s - Current session   " % WriteCurrentFormattedTime())
    sys.stdout.write("%s - Total time " % WriteFormattedTime())
    sys.stdout.flush()
    time.sleep(1)
    


