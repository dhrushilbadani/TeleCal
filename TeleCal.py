import httplib2
import os
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
import datetime
from bs4 import BeautifulSoup
import helpers

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'TeleCal'


def edit(time):
    s = time.replace('AM','').replace('PM','')
    return s


def get_credentials(choice):
    """Gets valid user credentials from storage.

    If the user wants new credentials or nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if choice == 'new':
        condition = True
    else:
        condition = not credentials or credentials.invalid
        if condition:
            print 'Invalid or non-existent Google credentials.'
    if condition:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatability with Python 2.6
            credentials = tools.run(flow, store)
        print 'Storing credentials to ' + credential_path
    return credentials

def createEvents(service, stopDate):
    '''
    Gets data from the TeleBears HTML, and adds each class as a recurring event to
    the logged-in user's Google Calendar using the Google Calendar API.
    '''
    soup = BeautifulSoup(open(os.path.realpath('TeleBears.html')), "html.parser")
    table = soup.find('table', attrs={'class':'class-list-content'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr', attrs={'class':'tbl-data'})
    for row in rows:
        info = row.find_all('td')
        cols = [ele.text.strip().replace('u','') for ele in info]
        course = (cols[1] + ' ' + cols[2]).split(' ')
        descr = course[0] + ' ' + course[1] + ' ' + course[3]
        print 'Adding', descr, 'to your Google Calendar..'
        days = helpers.getDays(cols[5])
        time = str(cols[6])
        ampm = time[-2:]
        time = time.split('-')
        begin = time[0]
        beginAm = 'AM' in begin
        begin = begin.split(':')
        beginArr = [int(edit(begin[0])), int(edit(begin[1]))]
        end = time[1]
        endPm = 'PM' in end
        end = end.split(':')
        endArr = [int(edit(end[0])), int(edit(end[1]))]
        if endPm is True and endArr[0] != 12 :
            endArr = [endArr[0] + 12, endArr[1]]
            if not beginAm and beginArr[0] != 12:
                beginArr = [beginArr[0] + 12, beginArr[1]]
        location = cols[7]
        for d in days:
            next_day = helpers.next_weekday(d)
            startTime = next_day.replace(hour = beginArr[0], minute = beginArr[1], second = 0).isoformat()
            startTime = startTime[0: startTime.rfind(':')+3]
            endTime = next_day.replace(hour = endArr[0], minute = endArr[1], second = 0).isoformat()
            endTime = endTime[0: endTime.rfind(':')+3]
            event = {
                  'summary': descr,
                  'location': location,
                  'start': {
                    'dateTime': startTime,
                    'timeZone': 'America/Los_Angeles'
                  },
                  'end': {
                    'dateTime': endTime,
                    'timeZone': 'America/Los_Angeles'
                  },
                  'recurrence': [
                    'RRULE:FREQ=WEEKLY;UNTIL='+stopDate,
                  ]
                }
            recurring_event = service.events().insert(calendarId='primary', body=event).execute()
    print 'Done!'


def main():
    credChoice = 'invalid'
    while credChoice == 'invalid':
        choice = raw_input('Do you want to use existing Google credentials stored on your system? [Y/N]')
        if choice == 'N' or choice == 'n':
            credChoice = 'new'
        elif choice == 'Y' or choice == 'y':
            credChoice = 'old'
        else:
            credChoice = 'invalid'
    validDate = False
    while not validDate:
        stopDate = raw_input('Enter the date your semester ends: [YYYY-MM-DD, eg. 2015-12-05]')
        try:
            helpers.validateDate(stopDate)
            validDate = True
        except ValueError:
            print 'Invalid date, please try again.'
            validDate = False
    stopDate = stopDate.replace('-','') + 'T000000Z'
    credentials = get_credentials(credChoice)
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    createEvents(service, stopDate)

if __name__ == '__main__':
    main()
