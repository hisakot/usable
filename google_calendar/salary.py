from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

from tkinter import *
import tkinter as tk
import calendar

# read calendar id
with open('calendarId.txt', 'r') as f:
    CALENDARID = f.readline()

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def google_calendar(tmin, tmax):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(
            calendarId=CALENDARID,
            timeMin=tmin, 
            timeMax=tmax, 
            maxResults=20,
            singleEvents=True,
            orderBy='startTime'
            ).execute()
    events = events_result.get('items', [])

    return events

def string2datetime():
    year = int(entry_y.get())
    month = int(entry_m.get())
    tmin = datetime.datetime(year, month, 1).isoformat() + 'Z'
    tmax = datetime.datetime(year, month, calendar.monthrange(year, month)[1]).isoformat() + 'Z'

    events = google_calendar(tmin, tmax)

    salary = 0
    records = ""
    for i, event in enumerate(events):
        start = event['start'].get('dateTime', event['start'].get('datetime'))
        start = datetime.datetime.fromisoformat(start)
        end = event['end'].get('dateTime', event['end'].get('datetime'))
        end = datetime.datetime.fromisoformat(end)

        work_time = end - start
        work_min = work_time.total_seconds() / 60
        if work_min > 60 * 8:
            work_min -= 60
        record = str(start.year) + '/' + str(start.month).zfill(2) + '/' + str(start.day).zfill(2) + ' ' + str(start.hour).zfill(2) + ':' + str(start.minute).zfill(2) + '-' + str(end.hour).zfill(2) + ':' + str(end.minute).zfill(2) + '  :  ' + str(int(work_min / 60)) + ':' + str(int(work_min % 60)).zfill(2) + '  ' + start.strftime('%a') + '\n'

        records += record

        if start.strftime('%a') == "Sat" or start.strftime('%a') == "Sun":
            salary += int(work_min * 1200 / 60)
        else:
            salary += int(work_min * 1100 / 60)

    label_time.config(text=str(records))
    label_money.config(text=str(salary))

if __name__ == '__main__':
    # make winndow
    root = tk.Tk()
    # winsow name
    root.title(u"calndar")
    # window size
    root.geometry("500x380")

    # year
    label_y = tk.Label(text="year")
    label_y.place(x=10, y=10)
    entry_y = tk.Entry(width=4)
    entry_y.place(x=45, y=10)
    # month
    label_m = tk.Label(text="month")
    label_m.place(x=90, y=10)
    entry_m = tk.Entry( width=2)
    entry_m.place(x=140, y=10)
    # unit
    label_yen = tk.Label(text="yen")
    label_yen.place(x=450, y=330)
    # work day
    label_time = tk.Label(root)
    label_time.place(x=10, y=50)
    label_money = tk.Label(root)
    label_money.place(x=400, y=330)
    # date button
    button = tk.Button(root, text="Enter", command=string2datetime)
    button.place(x=200, y=10)

    # stay window status
    root.mainloop()
