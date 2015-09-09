# TeleCal
Integrates Cal students' class schedules (from TeleBears) with their Google Calendars. In Python.

This is a Python tool to integrate Cal students' class schedules (from [TeleBears](https://telebears.berkeley.edu/telebears/home) with their [Google Calendars](https://www.google.com/calendar/) using the [Google Calendar API for Python](https://developers.google.com/google-apps/calendar/quickstart/python). Since there's no available
API for TeleBears as of now and scraping the website with just the [class list URL](https://telebears.berkeley.edu/telebears/enrollment?action=class_list) is impossible (let me know if you do succeed though; I tried the Selenium, requests, BeautifulSoup and mechanize libraries to no avail!), students will instead simply have to save the webpage of their [class list](https://telebears.berkeley.edu/telebears/enrollment?action=class_list)
in the TeleCal directory. 

You'll need the [Google Calendar API](https://developers.google.com/google-apps/calendar/quickstart/python) (you may skip Step 1) and [BeautifulSoup](https://pypi.python.org/pypi/beautifulsoup4) to run this.

##Usage
* Go to Terminal and type the following:
```
    git remote add telecal https://github.com/dhrushilbadani/TeleCal.git
    git pull telecal master
    cd TeleCal
```
* Go to your [TeleBears class list](https://telebears.berkeley.edu/telebears/enrollment), and save the page as an HTML file in the TeleCal/ directory.
* Run TeleCal.py from Terminal:
    ```
    python TeleCal.py
    ```
* You'll be provided with two choices:
  * Use existing credentials that TeleCal stores securely on your machine (if they exist), or
  * Provide new credentials by logging in with OAuth2 authentication to his/her Google account in a browser window that'll automatically open up.
* You'll then be asked to provide the end date for the semester, and TeleCal will then integrate your class schedule into your Google Calendar. If you've synced your smartphone's calendar with your Google account, it'll show up there as well!
