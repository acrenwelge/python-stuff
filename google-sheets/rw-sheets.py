from customauth import *
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SHEET_ID = '1eCD-lj0TLqOa8RzkuWZVOY0UVYxgUaYie9t7fnWs3_g'
RANGE_NAME = 'Week 1!A2:E'

def main():
  sheet = authorize()
  print('Using sheet ' + SHEET_ID)

  while True:
    print("Choose:")
    print("1. Write a new question & answer")
    print("2. Read the last Q&A")

  result = sheet.values().get(spreadsheetId=SHEET_ID, range=RANGE_NAME).execute()
  values = result.get('values', [])

  option = input()

  if option == 1:
    q = raw_input("What is your question?")
    ans = raw_input("What is your answer?")
    sheet.values.append(spreadsheetId=SHEET_ID, range=RANGE_NAME, body = {'data': [q, ans]})
  elif option == 2:
    print(values[-1])
  

  print("Question \t \t Answer")
  for row in values:
    print(row[0] + "\t\t" + row[1])
  


if __name__ == '__main__':
  main()
