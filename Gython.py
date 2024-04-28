### GYTHON.PY ###
# Welcome to Gython! Where you can make new projects using new commands, functions and variables! Hope you have fun using the Gython Add-On!

import sys
import os
import random as __random__
import time as __time__
from datetime import date as __date__
from datetime import datetime as __datetime__
from typing_extensions import *
from colorama import Fore as __Fore__
from colorama import Style as __Style__
from colorama import Back as __Back__
import webbrowser as __webbrowser__
import requests as __requests__
from bs4 import BeautifulSoup as __BeautifulSoup__
from random import randint as __randint__
from cursor import cursor as __cursor__
import numpy as __np__
import pydebug as __pydebug__
# Version
Version = "Beta 1.0.0"
# Welcome to Gython message
WelcomeMessage = """Welcome to Gython! Gython is a special Add-On for Python so you can code using new functions and Variables!"""
# # Classes
class ColorPanel:
  GREEN = f"{__Fore__.GREEN}"
  RESET = f"{__Style__.RESET_ALL}"
  RESETCOLOR = f"{__Fore__.RESET}"
  RED  = f"{__Fore__.RED}"
  BLUE = f"{__Fore__.BLUE}"
  YELLOW = f"{__Fore__.YELLOW}"
  CYAN = f"{__Fore__.CYAN}"
  MAGENTA = f"{__Fore__.MAGENTA}"
  WHITE = f"{__Fore__.WHITE}"
  BLACK = f"{__Fore__.BLACK}"
  LIGHTBLACK = f"{__Fore__.LIGHTBLACK_EX}"
  LIGHTBLUE = f"{__Fore__.LIGHTBLUE_EX}"
  LIGHTCYAN = f"{__Fore__.LIGHTCYAN_EX}"
  LIGHTGREEN = f"{__Fore__.LIGHTGREEN_EX}"
  LIGHTMAGENTA = f"{__Fore__.LIGHTMAGENTA_EX}"
  LIGHTRED = f"{__Fore__.LIGHTRED_EX}"
  LIGHTWHITE = f"{__Fore__.LIGHTWHITE_EX}"
  LIGHTYELLOW = f"{__Fore__.LIGHTYELLOW_EX}"
  class BackgroundColors:
    LIGHTGREEN = f"{__Back__.LIGHTGREEN_EX}"
    BLACK = f"{__Back__.BLACK}"
    RESET = f"{__Back__.RESET}"
    GREEN = f"{__Back__.GREEN}"
    BLUE = f"{__Back__.BLUE}"
    RED = f"{__Back__.RED}"
    YELLOW = f"{__Back__.YELLOW}"
    CYAN = f"{__Back__.CYAN}"
    MAGENTA = f"{__Back__.MAGENTA}"
    WHITE = f"{__Back__.WHITE}"
    LIGHTBLACK = f"{__Back__.LIGHTBLACK_EX}"
    LIGHTBLUE = f"{__Back__.LIGHTBLUE_EX}"
    LIGHTCYAN = f"{__Back__.LIGHTCYAN_EX}"
    LIGHTGREEN = f"{__Back__.LIGHTGREEN_EX}"
    LIGHTMAGENTA = f"{__Back__.LIGHTMAGENTA_EX}"
    LIGHTRED = f"{__Back__.LIGHTRED_EX}"
    LIGHTWHITE = f"{__Back__.LIGHTWHITE_EX}"
    LIGHTYELLOW = f"{__Back__.LIGHTYELLOW_EX}"

class TextEditPanel:
  ITALIC = "\x1B[3m"
  BOLD = "\x1B[1m"
  ITALIC_END = "\x1B[0m"
  BOLD_END = "\x1B[0m"
  UNDERLINE = "\x1B[4m"
  UNDERLINE_END = "\x1B[0m"
class GyWebPackages:
  import os
  import sys
  import webbrowser as web
  import flask 
  import django as dj
  import flask_cors as flc
  import hug 
  import flask_restful as frl
  import cherrypy 
  import bottle 
# ----------------------------------------------------------------------------------
Credits = f"""-----------------------------------------------
Green's Coding: 
https://replit.com/@GreenGaming6 (Creator/Publisher)
Project On Replit:
https://replit.com/@GreenGaming6/Gython (Project)
-------------------------------------------------------------------------
This is an open-source repl made on REPLIT.com, Please do not edit or do anything and publish without permission.
If you make a project using this please do credits [if you dont want it's ok], Thanks for reading."""
# Error Codes
__ERRORCODE001 = f"""
{__Fore__.RED}(CodeError):
(PrintDone) Value must be a Boolean Value 'True' or 'False', Please Try Again.
ErrorCode: 001
{__Fore__.RESET}"""
__ERRORCODE002 = f"""
{__Fore__.RED}(CodeError):
Value must be an Integer Value, Please Try Again.
ErrorCode: 002
{__Fore__.RESET}"""
__ERRORCODE003 = f"""
{__Fore__.RED}{__Style__.BRIGHT}(CodeError):
Value must be a String Value, Please Try Again.
ErrorCode: 003
{__Fore__.RESET}{__Style__.RESET_ALL}"""

__ERRORCODE004 = f"""
{__Fore__.RED}(CodeError):
Value must be a List Value, Please Try Again.
ErrorCode: 004
{__Fore__.RESET}"""


__ERRORCODE005 = f"""
{__Fore__.RED}{__Style__.BRIGHT}(CodeError):
Invalid Value, Please Try Again.
ErrorCode: 005
{__Fore__.RESET}{__Style__.RESET_ALL}"""

__ERRORCODE006 = f"""
{__Fore__.RED}{__Style__.BRIGHT}(CodeError):
Unreachable or No Value, Please Try Again.
ErrorCode: 006
{__Fore__.RESET}"""

__ERRORCODE007 = f"""
{__Fore__.RED}{__Style__.BRIGHT}(CodeError):
Value/File does not exist, Please Try Again.
ErrorCode: 007
{__Fore__.RESET}"""

__ERRORCODE008 = f"""
{__Fore__.RED}(CodeError):
Value does not exist, Use 1-5, Please Try Again.
ErrorCode: 008
{__Fore__.RESET}"""

__ERRORCODE009 = f"""
{__Fore__.RED}{__Style__.BRIGHT}(MajorError)
Could not understand, Please try again
{__Fore__.RESET}{__Style__.RESET_ALL}"""

__ERRORCODE0010 = f"""
{__Fore__.RED}{__Style__.BRIGHT}(MajorError)
[soon!]
{__Fore__.RESET}{__Style__.RESET_ALL}"""
# -----------------------------------------------------
class GyPlus:
  def SayErrorCode(errorcode):
    if errorcode == "001":
      Say(__ERRORCODE001)
    elif errorcode == "002":
      Say(__ERRORCODE002)
    elif errorcode == "003":
      Say(__ERRORCODE003)
    elif errorcode == "004":
      Say(__ERRORCODE004)
    elif errorcode == "005":
      Say(__ERRORCODE005)
    elif errorcode == "006":
      Say(__ERRORCODE006)
  def Warn(warn, level):
    if level == 1 or level == "1":
      Say(f"{ColorPanel.LIGHTRED}{warn}{ColorPanel.RESETCOLOR}")
    elif level == 2 or level == "2":
      Say(f"{ColorPanel.LIGHTYELLOW}{warn}{ColorPanel.LIGHTYELLOW}")
    elif level == 3 or level == "3":
      Say(f"{ColorPanel.YELLOW}{warn}{ColorPanel.RESETCOLOR}")
    elif level == 4 or level == "4":
      Say(f"{ColorPanel.RED}{warn}{ColorPanel.RESETCOLOR}")
    elif level == 5 or level == "5":
      Say(f"{ColorPanel.MAGENTA}{warn}{ColorPanel.RESETCOLOR}")
    elif level:
      Say(__ERRORCODE008)
######### Functions #########
# Makes Mathematical Problems
def Maths(num1, num2, operator):
  num1 = int(num1)
  num2 = int(num2)
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*" or "x".lower():
    return num1 * num2
  elif operator == "/":
    return num1 / num2
  elif operator == "^":
    return num1 ^ num2
# Basically the print() function
def Say(string):
  string = str(string)
  print(string)
# Exits Gython
def Exit():
  """
  This function exits Gython/Console
  """
  sys.exit()
# Clears the console
def Clear():
  """
  Clears the console
  """
  os.system("clear")
# basically the time.sleep() function
def Wait(seconds):
  """
  Waits for a specific time."""
  __time__.sleep(int(seconds))
# Sets a Timer
def timer(seconds, minutes, hours, days, PrintDone):
  """
  timer(seconds, minutes, hours, days, When Done Print?)
  Waits the specified seconds/minutes/hours/days, also you can set it so it says when done"""
  seconds = int(seconds)
  seconds = minutes/60
  seconds = hours/3600
  seconds = days/86400
  __time__.sleep(seconds)
  PrintDone = bool(PrintDone)
  if PrintDone == True:
    print("Timer Completed!")
  elif PrintDone == False:
    return
  else:
    Say(f"{__ERRORCODE001}")
# Gets a Random Number
def random(min, max):
  """
  random(min, max)
  Gets a random number between the specified minimum number and the maximum number"""
  min = int(min)
  max = int(max)
  __random__.randint(min, max)

# def CreateDictionary(key, value):
#   """
#   CreateDictionary(key, value)"""
#   key = str(key)
#   value = str(value)
#   dictionary = {key: value}
#   return dictionary
# Checks if value is true
def IsTrue(value):
  if value == True:
    Say(f"{value} is True")
  elif value == False:
    Say(f"{value} is False")
  elif value:
    Say(f"{value} is not True and is not False")
# Checks if value is false
def IsFalse(value):
  if value == True:
    Say(f"{value} is True")
  elif value == False:
    Say(f"{value} is False")
  elif value:
    Say(f"{value} is not True and is not False")
# credits
def credit():
  """Says the Credits!"""
  Say(Credits)

# def delete(variable):
#   """
#   Deletes the specified Variable"""
#   del variable
# makes a folder
def makefolder(directory):
  """Makes a Folder/Directory"""
  os.mkdir(directory)
  Say("Made Folder Successfully.")
# makes a file
def makefile(file):
  """Makes a file."""
  os.mkfifo(file)
  Say("Made File Successfully")
# deletes a file
def deletefile(file):
  """Deletes a file."""
  os.remove(file)
  Say("Removed File Successfully")
# deletes a folder
def deletefolder(folder):
  """Deletes the specified Folder."""
  os.removedirs(folder)
  Say("Removed Folder Successfully")

# def getdir(filedir):
#   """Gets current directory (Folder) where the File is"""
#   directory = os.getcwd()
#   Say(f"The Current Directory is {directory}")

# reads a file
def readfile(file):
  """Reads the specified file."""
  file = str(file)
  with open(file, "r") as f:
    contents = f.read()
    Say(f"The contents of the file {file} are:\n{contents}")
# writes a file
def writefile(file, text):
    """Writes a file"""
    file = str(file)
    with open(file, "w") as f:
        f.write(text)
    Say(f"The file {file} has been written with the text {text} ")
# removes a file
def removedir(directory):
  """Removes the specified Directory"""
  os.rmdir(directory)
  Say("Removed Directory Successfully")
# pops a value from a list
def pop(list, index):
  """Gets the index from the list"""
  list = list
  index = int(index)
  list.pop(index)
  Say(f"Popped {index} from {list}")
# adds a value to a list
def addvalue(list, value):
  """Adds the specified value to the specified list."""
  list = list
  value = value
  list.append(value)
# removes a value from a list
def removevalue(list, value):
  """Removes a value from a list."""
  list=list
  value = value
  list.remove(value)
# gets the length
def GetLength(value):
  """Gets the length of the specified value."""
  value = value
  length = len(value)
# web scrapes a selected website\
def webscrape(url):
  """Webscrapes the specified website."""
  response = __requests__.get(url)
  html_content = response.text
  soup = __BeautifulSoup__(html_content, "html.parser")
  return soup.prettify()
# opens a file/website
def openurl(url):
  """Opens the specified url(website)/file."""
  url = str(url)
  __webbrowser__.open(url)
  if url == "" or url == "template".lower() or url == "temp".lower() or url == "?" or url == "help".lower():
    __webbrowser__.open("https://sites.google.com/view/gythontemplate/home")
# gets the current time
def getcurrenttime():
  """Gets the current time"""
  return __time__.time
# gets the current date
def getcurrentdate():
  """Gets the current date."""
  return __date__.today
# gets current datetime
def getcurrentdatetime():
  """gets current datetime."""
  return __datetime__.now
# gets current year
def getcurrentyear():
  """gets current year."""
  # Basically useless. #
  return __date__.year
# gets current day
def getcurrentday():
  """Gets the current day."""
  return __date__.day
# gets current month
def getcurrentmonth():
  """Gets the current month"""
  return __date__.month
# gets current hour
def getcurrenthour():
  """Gets the current hour."""
  return __datetime__.hour
# gets current minute
def getcurrentminute():
  """Gets the current minute"""
  return __datetime__.minute
# gets current second
def getcurrentsecond():
  """Gets the current second"""
  return __datetime__.second
# gets current microsecond
def getcurrentmicrosecond():
  """Gets the current microsecond"""
  return __datetime__.microsecond
# performs a search on google
def search(query, search_engine):
  """Performs searches on the specified search engine."""
  if search_engine == "google".lower():
    __webbrowser__.open(f"https://www.google.com/search?q={query}")
  elif search_engine == "bing".lower():
    __webbrowser__.open(f"https://www.bing.com/search?q={query}")
  elif search_engine == "duckduckgo".lower():
    __webbrowser__.open(f"https://duckduckgo.com/?va=e&t=hp&q={query}&ia=web")
  elif search_engine == "yahoo".lower():
    __webbrowser__.open(f"https://search.yahoo.com/search?p={query}")
  elif search_engine == "yandex".lower():
    __webbrowser__.open(f"https://yandex.com/search/?text={query}&lr=41030&search_source=yacom_desktop_common")
  elif search_engine == "ask".lower():
    __webbrowser__.open(f"https://www.ask.com/web?q={query}&ad=SEO&o=779176")
  elif search_engine == "baidu".lower():
    __webbrowser__.open(f"https://www.baidu.com/s?wd={query}")
  elif search_engine == "yep".lower():
    __webbrowser__.open(f"https://yep.com/web?q={query}")
  elif search_engine:
    Say(__ERRORCODE005)
  else:
    Say(__ERRORCODE009)
# Evaluates a string
def evaluate(string):
  """Evaluates the specified string."""
  string = str(string)
  return eval(string)
# makes a random number
def Random(min, max):
  """Gets a random number between the specified minimum number and the maximum number"""
  min = int(min)
  max = int(max)
  return __random__.randint(min, max)
# gets a random choice
def SpinWheel(list):
  """Gets random value from the specified list."""
  return __random__.choice(list)
# gets a vowel
def GetVowel():
  """Gets a random vowel..."""
  return __random__.choice("aeiou")
# gets a consonant
def GetConsonant():
  """Gets a random consonant..."""
  return __random__.choice("bcdfghjklmnpqrstvwxyz")
# gets a random letter
def getrandomletter():
  """Gets a random letter"""
  return __random__.choice("abcdefghijklmnopqrstuvwxyz")
# makes a password protected thing
def PasswordProtect(password, value, get_input, SayWhenInCorrect):
  """Password protects the specified value."""
  password = str(password)
  if get_input == password:
    Say(value)
  elif get_input:
    if SayWhenInCorrect == "True" or SayWhenInCorrect == True:
      Say(f"Incorrect Password/Passcode")
    elif SayWhenInCorrect == "False" or SayWhenInCorrect == False:
      return password
    elif SayWhenInCorrect:
      Say(__ERRORCODE005)
    else:
      Say(__ERRORCODE009)
  else:
    Say(__ERRORCODE009)
# makes tasks
def WaitForTask(task, time, message):
  """Waits for the specified task then sends a message"""
  strtask = str(task)
  inttime = int(time)
  time.sleep(inttime)
  Say(f"{message} {task}!")
# executes code
def ExecCode(code):
  """Executes the specified code."""
  code = str(code)
  exec(code)
#
# def DebugCode(code):
#   """Debugs code?"""
#   code = str(code)
#   return __pydebug__.debug(code)

# qoutes a string
def QuoteString(string, type):
  """Quotes a string. one/two or 1/2 and other stuff."""
  streng = str(string)
  if type == "one" or type == "1" or type == "single" or type == "single quote" or type == "singlequote":
            string = f'"{streng}"'  
  elif type == "two" or type == "2" or type == "double" or type == "double quote" or type == "doublequote":
    string = f"'{streng}'"
  return string
#
