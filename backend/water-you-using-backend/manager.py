import constants
import demjson
import shortuuid
import bcrypt
import time
from getpass import getpass

#Register a new user to the database with their username, password, and UUID
def register_user(username, password):
    #Ensure the username is available
    if get_uuid(username) != constants.USERNAME_NOT_FOUND:
        return "Username unavailable";

    #Get the users.json file
    json = get_json_file(constants.USERS_FILE_NAME);
    
    #Hash and salt the password
    password_hash = hash_password(password);
    
    #Generate a random UUID with 8 characters
    uuid = shortuuid.ShortUUID().random(length=8);
    
    #Save the user object with their username and hash
    json.append({"uuid":uuid, "username":username, "password_hash":password_hash});
    
    #Add the user to the master user file
    update_json_file(constants.USERS_FILE_NAME, json);
    
    #Generate the user's event log file
    event_file = [];
    update_json_file(constants.EVENTS_DIR_NAME + uuid + '.json', event_file);
    
    return "Registration complete";

#Returns LOGIN_SUCCESS if the user's credentials are valid and LOGIN_FAILED if not
def login_user(username, password):
    user = get_user_from_username(username);
    if verify_password(user.get('password_hash'), password) == True:
        return constants.LOGIN_SUCCESS;
    else:
        return constants.LOGIN_FAILED;

#Returns the python object for the found user
def get_user(uuid):
    json = get_json_file(constants.USERS_FILE_NAME);
    found_user = {"uuid":"NOT_FOUND", "username":"NOT_FOUND","password_hash":"NOT_FOUND"};
    # Using for loop 
    for user in json: 
        if user.get('uuid') == uuid:
            found_user = user;
            print("Found user: " + user.get("username"));
            break;
    return found_user;
    
#Get the user's uuid from a username
def get_uuid(username):
    json = get_json_file(constants.USERS_FILE_NAME);
    for user in json: 
        if user.get('username') == username:
            found_user = user;
            return user.get('uuid');
            
    return constants.USERNAME_NOT_FOUND;

#Returns the python object for the found user
def get_user_from_username(username):
    json = get_json_file(constants.USERS_FILE_NAME);
    found_user = {"uuid":"NOT_FOUND", "username":"NOT_FOUND","password_hash":"NOT_FOUND"};
    #For each user, 
    for user in json: 
        if user.get('username') == username:
            found_user = user;
            print("Found user with uuid: " + user.get("uuid"));
            break;
    return found_user;

def add_event(username, device, start_time, end_time, volume):
    json = get_json_file(constants.EVENTS_DIR_NAME + get_uuid(username) + '.json');
    if get_uuid(username) == constants.USERNAME_NOT_FOUND:
        return constants.USERNAME_NOT_FOUND;
    json.append({"device":device, "start_time":start_time, "end_time":end_time, "volume":volume});
    update_json_file(constants.EVENTS_DIR_NAME + get_uuid(username) + '.json', json);
    return constants.ADD_EVENT_SUCCESS;

#For the given user, return a JSON file containing all water events for the given data point definition.
#Note: The actual breakdowns by each period (for use in graphs) will be calculated with this data on the client.
#If HOURLY_DATA_POINT, every event within the past 24 hours will be returned
#If DAILY_DATA_POINT, every event within the past week will be returned
#If WEEKLY_DATA_POINT, every event within the past month will be returned
#If MONTHLY_DATA_POINT, every event within the past year will be returned
#If YEARLY_DATA_POINT, every event within the past 10 years will be returned
def get_event_data(username, data_points):
    json = get_json_file(constants.EVENTS_DIR_NAME + get_uuid(username) + '.json');
    if get_uuid(username) == constants.USERNAME_NOT_FOUND:
        return constants.USERNAME_NOT_FOUND;
    epoch_time = int(time.time())
    found_events = [];
    if data_points == constants.HOURLY_DATA_POINT:
        #Loop through all events. If any event is within the past day, add it to the list.
        for event in json:
            if epoch_time - int(event.get('start_time')) <= constants.SECONDS_IN_DAY:
                found_events.append(event);
    if data_points == constants.DAILY_DATA_POINT:
        #Loop through all events. If any event is wihin the past week, add it to the list.
        for event in json:
            if epoch_time - int(event.get('start_time')) <= constants.SECONDS_IN_WEEK:
                found_events.append(event);
    if data_points == constants.WEEKLY_DATA_POINT:
        #Loop through all events. If any event is wihin the past month, add it to the list.
        for event in json:
            if epoch_time - int(event.get('start_time')) <= constants.SECONDS_IN_MONTH:
                found_events.append(event);
    if data_points == constants.MONTHLY_DATA_POINT:
        #Loop through all events. If any event is wihin the past year, add it to the list.
        for event in json:
            if epoch_time - int(event.get('start_time')) <= constants.SECONDS_IN_YEAR:
                found_events.append(event);
    if data_points == constants.YEARLY_DATA_POINT:
        #Loop through all events. If any event is wihin the past 10 years, add it to the list.
        for event in json:
            if epoch_time - int(event.get('start_time')) <= constants.SECONDS_IN_YEAR * 10:
                found_events.append(event);            
    return demjson.encode(found_events);
        
#For the given user, return a JSON file containing all water events for the given data point definition and device.
#Note: This functions basically the same way as get_event_data
def get_event_data_device(username, device, data_points):
    json = get_json_file(constants.EVENTS_DIR_NAME + get_uuid(username) + '.json');
    if get_uuid(username) == constants.USERNAME_NOT_FOUND:
        return constants.USERNAME_NOT_FOUND;
    epoch_time = int(time.time())
    found_events = [];
    if data_points == constants.HOURLY_DATA_POINT:
        #Loop through all events. If any event is within the past day, add it to the list.
        for event in json:
            if epoch_time - int(event.get('start_time')) <= constants.SECONDS_IN_DAY and event.get('device') == device:
                found_events.append(event);
    if data_points == constants.DAILY_DATA_POINT:
        #Loop through all events. If any event is wihin the past week, add it to the list.
        for event in json:
            if epoch_time - int(event.get('start_time')) <= constants.SECONDS_IN_WEEK and event.get('device') == device:
                found_events.append(event);
    if data_points == constants.WEEKLY_DATA_POINT:
        #Loop through all events. If any event is wihin the past month, add it to the list.
        for event in json:
            if epoch_time - int(event.get('start_time')) <= constants.SECONDS_IN_MONTH and event.get('device') == device:
                found_events.append(event);
    if data_points == constants.MONTHLY_DATA_POINT:
        #Loop through all events. If any event is wihin the past year, add it to the list.
        for event in json:
            if epoch_time - int(event.get('start_time')) <= constants.SECONDS_IN_YEAR and event.get('device') == device:
                found_events.append(event);
    if data_points == constants.YEARLY_DATA_POINT:
        #Loop through all events. If any event is wihin the past 10 years, add it to the list.
        for event in json:
            if epoch_time - int(event.get('start_time')) <= constants.SECONDS_IN_YEAR * 10 and event.get('device') == device:
                found_events.append(event);            
    return demjson.encode(found_events);
    
    
#Returns an array of floats with the total water usage in the last time for the device
def get_last_time_volume(username, device):
    json = get_json_file(constants.EVENTS_DIR_NAME + get_uuid(username) + '.json');
    last_hour_volume = 0.0;
    last_day_volume = 0.0;
    last_week_volume = 0.0;
    last_month_volume = 0.0;
    last_year_volume = 0.0;
    epoch_time = int(time.time());
    for event in json:
            if epoch_time - int(event.get('start_time')) <= constants.SECONDS_IN_HOUR and event.get('device') == device:
                last_hour_volume = last_hour_volume + float(event.get('volume'));
            if epoch_time - int(event.get('start_time')) <= constants.SECONDS_IN_DAY and event.get('device') == device:
                last_day_volume = last_day_volume + float(event.get('volume'));  
            if epoch_time - int(event.get('start_time')) <= constants.SECONDS_IN_WEEK and event.get('device') == device:
                last_week_volume = last_week_volume + float(event.get('volume'));  
            if epoch_time - int(event.get('start_time')) <= constants.SECONDS_IN_MONTH and event.get('device') == device:
                last_month_volume = last_month_volume + float(event.get('volume'));
            if epoch_time - int(event.get('start_time')) <= constants.SECONDS_IN_YEAR and event.get('device') == device:
                last_year_volume = last_year_volume + float(event.get('volume'));
    return demjson.encode([{"hour":last_hour_volume, "day":last_day_volume, "week":last_week_volume, "month":last_month_volume, "year":last_year_volume}]);
    
#breakdown array response thing for Kai (one-object JSON array, keys are: (24 key hour array, 7 item day array)
def get_breakdown(username, data_points):
    json = get_json_file(constants.EVENTS_DIR_NAME + get_uuid(username) + '.json');
    if get_uuid(username) == constants.USERNAME_NOT_FOUND:
        return constants.USERNAME_NOT_FOUND;
    epoch_time = int(time.time())
    hourly_volume = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    daily_volume = [0, 0, 0, 0, 0, 0, 0];
    
    #Return a 24-key JSON object for each hour of the past day containing the total volume for that hour
    if data_points == constants.HOURLY_DATA_POINT:
        #Loop through all events. If any event is within the past day, add it to the list.
        for event in json:
            timediff = epoch_time - int(event.get('start_time'));
            print("timediff: " + str(timediff));
            if timediff <= (constants.SECONDS_IN_HOUR * 24) and timediff > (constants.SECONDS_IN_HOUR * 23):
                hourly_volume[0] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 23) and timediff > (constants.SECONDS_IN_HOUR * 22):
                hourly_volume[1] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 22) and timediff > (constants.SECONDS_IN_HOUR * 21):
                hourly_volume[2] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 21) and timediff > (constants.SECONDS_IN_HOUR * 20):
                hourly_volume[3] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 20) and timediff > (constants.SECONDS_IN_HOUR * 19):
                hourly_volume[4] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 19) and timediff > (constants.SECONDS_IN_HOUR * 18):
                hourly_volume[5] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 18) and timediff > (constants.SECONDS_IN_HOUR * 17):
                hourly_volume[6] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 17) and timediff > (constants.SECONDS_IN_HOUR * 16):
                hourly_volume[7] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 16) and timediff > (constants.SECONDS_IN_HOUR * 15):
                hourly_volume[8] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 15) and timediff > (constants.SECONDS_IN_HOUR * 14):
                hourly_volume[9] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 14) and timediff > (constants.SECONDS_IN_HOUR * 13):
                hourly_volume[10] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 13) and timediff > (constants.SECONDS_IN_HOUR * 12):
                hourly_volume[11] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 12) and timediff > (constants.SECONDS_IN_HOUR * 11):
                hourly_volume[12] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 11) and timediff > (constants.SECONDS_IN_HOUR * 10):
                hourly_volume[13] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 10) and timediff > (constants.SECONDS_IN_HOUR * 9):
                hourly_volume[14] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 9) and timediff > (constants.SECONDS_IN_HOUR * 8):
                hourly_volume[15] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 8) and timediff > (constants.SECONDS_IN_HOUR * 7):
                hourly_volume[16] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 7) and timediff > (constants.SECONDS_IN_HOUR * 6):
                hourly_volume[17] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 6) and timediff > (constants.SECONDS_IN_HOUR * 5):
                hourly_volume[18] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 5) and timediff > (constants.SECONDS_IN_HOUR * 4):
                hourly_volume[19] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 4) and timediff > (constants.SECONDS_IN_HOUR * 3):
                hourly_volume[20] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 3) and timediff > (constants.SECONDS_IN_HOUR * 2):
                hourly_volume[21] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 2) and timediff > (constants.SECONDS_IN_HOUR * 1):
                hourly_volume[22] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_HOUR * 1) and timediff > (constants.SECONDS_IN_HOUR * 0):
                hourly_volume[23] += float(event.get('volume'));
        result = [{"h1":hourly_volume[0],"h2":hourly_volume[1],"h3":hourly_volume[2],"h4":hourly_volume[3],"h5":hourly_volume[4],"h6":hourly_volume[5],"h7":hourly_volume[6],"h8":hourly_volume[7],"h9":hourly_volume[8],"h10":hourly_volume[9],"h11":hourly_volume[10],"h12":hourly_volume[11],"h13":hourly_volume[12],"h14":hourly_volume[13],"h15":hourly_volume[14],"h16":hourly_volume[15],"h17":hourly_volume[16],"h18":hourly_volume[17],"h19":hourly_volume[18],"h20":hourly_volume[19],"h21":hourly_volume[20],"h22":hourly_volume[21],"h23":hourly_volume[22],"h24":hourly_volume[23]}];
        return demjson.encode(result);
         
    if data_points == constants.DAILY_DATA_POINT:
        for event in json:
            timediff = epoch_time - int(event.get('start_time'));
            if timediff <= (constants.SECONDS_IN_DAY * 7) and timediff > (constants.SECONDS_IN_DAY * 6) :
                daily_volume[0] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_DAY * 6) and timediff > (constants.SECONDS_IN_DAY * 5) :
                daily_volume[1] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_DAY * 5) and timediff > (constants.SECONDS_IN_DAY * 4) :
                daily_volume[2] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_DAY * 4) and timediff > (constants.SECONDS_IN_DAY * 3) :
                daily_volume[3] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_DAY * 3) and timediff > (constants.SECONDS_IN_DAY * 2) :
                daily_volume[4] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_DAY * 2) and timediff > (constants.SECONDS_IN_DAY * 1) :
                daily_volume[5] += float(event.get('volume'));
            if timediff <= (constants.SECONDS_IN_DAY * 1) and timediff > (constants.SECONDS_IN_DAY * 0) :
                daily_volume[6] += float(event.get('volume'));
        result = [{"d1":daily_volume[0],"d2":daily_volume[1],"d3":daily_volume[2],"d4":daily_volume[3],"d5":daily_volume[4],"d6":daily_volume[5],"d7":daily_volume[6]}];
        return demjson.encode(result);
        
    return daily_volume;

def get_last_event(username, password):
    if get_uuid(username) == constants.USERNAME_NOT_FOUND:
        return constants.USERNAME_NOT_FOUND;
    
    json = get_json_file(constants.EVENTS_DIR_NAME + get_uuid(username) + '.json');
    highest_event = [];
    highest_epoch = 0;
    for event in json:
        if int(event.get('end_time')) > highest_epoch:
            highest_event = event;
            highest_epoch = int(event.get('end_time'));
            
    return demjson.encode([{"text":"The most recent water usage was " + str(round(float(highest_event.get('volume')), 2)) + " gallons from " + highest_event.get('device') + " at " + time.strftime('%I:%M:%S %p', time.localtime(highest_epoch))}]);

def get_todays_usage(username, password):
    json = get_json_file(constants.EVENTS_DIR_NAME + get_uuid(username) + '.json');
    if get_uuid(username) == constants.USERNAME_NOT_FOUND:
        return constants.USERNAME_NOT_FOUND;
    epoch_time = int(time.time())
    usage = 0.0;
    for event in json:
            if epoch_time - int(event.get('start_time')) <= constants.SECONDS_IN_DAY:
                usage += float(event.get('volume'));
    return demjson.encode([{"text":str(round(usage, 2))}]);


#Clears the database
def clear():
    default_user_file = constants.DEFAULT_USER_JSON_OBJECT;
    update_json_file(constants.USERS_FILE_NAME, default_user_file);
    filelist = [ f for f in os.listdir(constants.EVENTS_DIR_NAME) if f.endswith(".json") and not f.endswith("gM9tZ4Au.json") ]
    for f in filelist:
        os.remove(os.path.join(constants.EVENTS_DIR_NAME, f))
    

#Returns the JSON file
def get_json_file(filename):
    file = open(filename, "r")
    json = demjson.decode(file.read());
    file.close();
    return json;

#Overwrites the given filename with the given json object
def update_json_file(filename, json_object):
    file = open(filename, "w+");
    file.write(demjson.encode(json_object));
    file.close();
    return filename;
    
    

#From https://www.vitoshacademy.com/hashing-passwords-in-python/
import hashlib, binascii, os
 
def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
 
def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password