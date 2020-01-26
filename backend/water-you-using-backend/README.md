#Backend repository for Water You Using

For development purposes, this will be hosted on
http://localhost:5000

#API Documentation:

Register a user account:
/register/[username]/[password]

Log in (Stateless - just used to verify username/password combo):
/login/[username]/[password]

Get username from UUID:
/getusername/[uuid]

Add a water event:
/addevent/[username]/[password]/[device]/[start_time]/[end_time]/[volume]/

Retrieve events:
/geteventdata/[username]/[password]/[data_point]

Where data_point is one of the following:

HOURLY_DATA_POINT: A JSON file containing all water events in the past day will be returned

DAILY_DATA_POINT:  A JSON file containing all water events in the past week will be returned

WEEKLY_DATA_POINT:  A JSON file containing all water events in the past month will be returned

MONTHLY_DATA_POINT:  A JSON file containing all water events in the past year will be returned

YEARLY_DATA_POINT:  A JSON file containing all water events in the past 10 years will be returned


Retrieve events for a certain device:
/geteventdata/[username]/[password]/[device]/[data_point]

Clear all user data (must be a user named admin):
/clear/admin/adminpass

Other than the device tag, this functions the same as the normal geteventdata endpoint.

This JSON data will be parsed on the client side, where it can be broken down into its respective data points.


Endpoints that return single values:

Return the total volume of water used in the last hour for the provided device
/lasttimevolume/[username]/[password]/[device]
[last hour, last day, last week, last month, last year]

Return a breakdown of water usage by hour or day (data_point must be HOURLY_DATA_POINT or DAILY_DATA_POINT)
/breakdown/[username]/[password]/[data_point]

Return a string containing a description of the most recent water usage
/getlastevent/[username]/[password]
