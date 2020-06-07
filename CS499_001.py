import json
from bson import json_util
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
import os

connection = MongoClient("mongodb://localhost:27017/")
db = connection['market']
collection = db['stocks']

#Develop a function to create a document in the MongoDB database city in the collection inspections.
#Be sure it can handle error conditions gracefully.
def insert_document(document):
  try:
    print("Insert Successful")
    result = collection.insert_one(document)
  except ValidationError as ve:
    abort(400, str(ve))
  print(result)

#:Develop a function to read a document in the MongoDB database city in the collection inspections.
#Be sure it can handle error conditions gracefully
def find_document(document):
  try:
    result=collection.find_one(document)
  except:
    result="Failed to Find Document"
  print(result)

#:Develop a function to update a document in the MongoDB database city in the collection inspections.
#Be sure it can handle error conditions gracefully
def update_document(keyvalue, setvalue):
  try:
    result=collection.update_one(keyvalue, setvalue)
    #Display Update Sucessful message
    print(result)
    #Display Updated JSON format result
    result=collection.find_one(keyvalue)
  except:
    result="Failed to Update Document"
  print(result)

#Develop a function to delete a document in the MongoDB database city in the collection inspections.
#Be sure it can handle error conditions gracefully
def delete_document(document):
  try:
    result=collection.delete_one(document)
  except:
    result="Failed to Delete Document"
  print(result)

def main():
  
  # 01:For insert
  print("01:Insert Section-----------------------------------")
  myDocument01 = { "date" : "2020-04-13",
               "Ticker" : "XYZ",
               "Volume":"0" }
  insert_document(myDocument01)
  print("Read the inserted document...")
  myDocument01 = { "Ticker" : "XYZ" }
  find_document(myDocument01)
  print("----------------------------------------------------")
  print("")
  
  # 02:For Update
  print("02:Update Section-----------------------------------")
  KEYVAL = { "Ticker" : "XYZ" }
  SETVAL = { "$set": { "Volume":"153" } }
  update_document(KEYVAL,SETVAL)
  print("----------------------------------------------------")
  print("")
  
  # 03:For Delete
  print("03:Delete Section-----------------------------------")
  myDocument01 = { "Ticker" : "XYZ" }
  print("Before...")
  find_document(myDocument01)
  print("")
  print("Delete Operation...")
  delete_document(myDocument01)
  print("----------------------------------------------------")
  print("")
  
  
main()