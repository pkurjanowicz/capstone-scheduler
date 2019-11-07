About:
    This application will allow users to save events that include the name of the event, and when it begins, with options to include when it ends and a short description of what the event is about. Users may also look up what time it is currently in different timezones.
-----------------------------------------------

Installation:
    This project is making use of the following:
    - pipenv(miniconda)(2018.05.18) (May have missed some usage along the way..)
    - sqlite3(miniconda)
    - flask(miniconda)(1.1.1)
    - node(v10.16.3)
    - python3(3.7.1)
-----------------------------------------------
Running Locally:

    To start everything, in terminal
        ctrl + shift + t (opens new terminal tab in ubuntu)

        To work with the database, from capstone-scheduler/db
        `sqlite3 userdata.db`

        To update changes to the project,
        from capstone-scheduler/client (it's set to --watch for changes and rebuild automatically.)
        `npm run build`

        To run the flask server,
        from capstone-scheduler/server
        `python main.py`

    To install new packages
        pipenv --three #installs new virtual environment for folder
        `pipenv istall 'package'`

-----------------------------------------------
Caveats:
    There is currently a known issue where axios responses don't always execute the code as expected. Sometimes the displayed list of events wont update when expected. An "Update my events" button was added to relieve this.

    Sometimes hitting the "Delete event" button malfunctions. Refreshing the page will restore it's functionality.
-----------------------------------------------
Next steps:
    This application could use a round of bug fixes to improve the responsiveness of expected results.
    
    The current user system is crude and insecure. Adding authentication would be necissary before deploying publicly.

    Improved layout and manual display options would greatly enhance the user experience for this application

    Graphical display for events would also improve user experience.

    Adding location information to each event would greatly improve practical uses in the real world.

    Adding more control over timezone information is also practical.

    Sharing events between users is a very useful feature to include after the previous changes have been made.
-----------------------------------------------
Other:

Using 'vue2-datepicker' and 'moment.js' to manage time in vue.

Using axios to handle routes and API calls.