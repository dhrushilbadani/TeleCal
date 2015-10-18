# TeleCal
Integrates Cal students' class schedules (from TeleBears) with their Google Calendars. In Python.

This is a Python tool to integrate Cal students' class schedules (from [TeleBears](https://telebears.berkeley.edu/telebears/home)) with their [Google Calendars](https://www.google.com/calendar/). No need to login to TeleBears to check your schedule ever again, it's all on your Google Calendar! 

Uses the [Google Calendar API](https://developers.google.com/google-apps/calendar/quickstart/python), [Selenium](http://selenium-python.readthedocs.org/), [PhantomJS](http://phantomjs.org/) and [BeautifulSoup](https://pypi.python.org/pypi/beautifulsoup4). Since there's no TeleBears API, I had to work my way around CalNet authentication using Selenium and PhantomJS ;)

##Usage
* Download the .zip file from the pane on the right >> , and extract its contents (Git folks can feel free to fork + pull instead).
* [Install pip](http://pip.readthedocs.org/en/stable/installing/), if you haven't already. It's rather useful.
* Install dependencies from within the extracted folder:
    ```
    pip install -r requirements.txt
    ```
*  Run TeleCal.py (in the extracted folder):
    ```
    python TeleCal.py
    ```
* You'll first be asked to enter your CalNet credentials -- I'm not storing them, I swear. Check the source code if you're worried!
* You'll then be provided with two choices for your Google Calendar:
  * Use existing Google credentials that TeleCal stores securely on your machine (if they exist), or
  * Provide new Google credentials by logging in with OAuth2 authentication to your Google account in a browser window that'll automatically open up after the next step.
* You'll then be asked to provide the end date for the semester.

Voilà, TeleCal will then integrate your class schedule into your Google Calendar! If you've synced your smartphone's calendar with your Google account, it'll show up there as well.

**I tried creating an executable using pyinstaller. Didn't work unfortunately!
