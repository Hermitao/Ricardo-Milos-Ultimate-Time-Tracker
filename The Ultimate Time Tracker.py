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

clear = lambda: os.system('cls')
startTime = time.time()

f = None
contents = None

# read or create file for elapsed time storage
try:
    with open("Time Elapsed.xml", "r+") as f:
        contents = f.read()
except FileNotFoundError:
    with open("Time Elapsed.xml", "w+") as f:
        contents = f.read()

if (contents != ""):
    startTime = time.time() - float(contents)

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# write a formatted version of time
def WriteTime():
    formattedTime = datetime.timedelta( seconds=(time.time() - startTime) )
    return str(formattedTime)

# store time data
def WriteToFile():
    f = open("Time Elapsed.xml", "r+")
    f.seek(0)
    f.write(str(time.time() - startTime))
    f.close()

while True:
    WriteToFile()
    sys.stdout.write("\r%s" % WriteTime())
    sys.stdout.flush()
    
    


