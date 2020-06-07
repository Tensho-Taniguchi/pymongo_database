import json
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']
import pprint
import os


#01:A function that takes as inputs numerical values for low and high
#finds documents for which the "50-Day Simple Moving Average" is between the low and high values and return the count
def find_Between50DayAvg(low, high):
  try:
    result=collection.find({'50-Day Simple Moving Average': { '$gte': low, '$lte': high }}).count()
  except:
    result="Failed to Find Document"
  print(result)

#02:A function that takes as input a string
# find documents for which the input string matches the document key "Industry"
# and returns the list of ticker symbols found to match that industry.
def find_listOfTickerFromIndustry(in_industry):
  TickerList = []
  try:
    for doc in collection.find({"Industry": in_industry }):
      TickerList.append(doc['Ticker'])
  except:
    result="Failed to Find Document"
  print(TickerList)

#03:create a function or method in Python or Java that will take as input a string. 
# The function or method will find documents for which the input string matches the document key "Sector"
# and returns the total outstanding shares grouped by document key "Industry"
def find_TotalShareOutstandingByIndustry(in_sector):
  ShareOutstandingList = []
  try:
    for doc in collection.aggregate([{ '$match': { "Sector": in_sector } },{ '$group': { "_id": "$Industry", "total": { '$sum': "$Shares Outstanding" } } }]):
      strTrgt=str(doc['_id'])+" : "+str(doc['total'])
      ShareOutstandingList.append(strTrgt)
  except:
    result="Failed to Find Document"
  print(ShareOutstandingList)

def main():
  
  #III.A.i - "50-Day Simple Moving Average"
  print("----------------------------------------------------")
  string_Low = 0.2
  string_High= 0.5
  find_Between50DayAvg(string_Low, string_High)
  print("----------------------------------------------------")
  print("")

  #III.A.ii - "Industory"
  print("----------------------------------------------------")
  string="Medical Laboratories & Research"
  find_listOfTickerFromIndustry(string)
  print("----------------------------------------------------")
  print("")
  
  #III.B    - "Aggregation Pipeline"
  print("----------------------------------------------------")
  string="Healthcare"
  find_TotalShareOutstandingByIndustry(string)
  print("----------------------------------------------------")
  print("")
  
main()