import demjson
import manager
import constants
from flask import Flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@cross_origin
@app.route('/')
def root_directory():
    return 'Water You Using Server v. 1.0'

@cross_origin
@app.route('/register/<string:username>/<string:password>')
def register(username, password):
    return manager.register_user(username, password);

@cross_origin
@app.route('/login/<string:username>/<string:password>')
def login(username, password):
    return manager.login_user(username, password);

@cross_origin
@app.route('/getusername/<string:uuid>')
def get_username(uuid):
    user = manager.get_user(uuid);
    return user.get('username');
    
@cross_origin
@app.route('/addevent/<string:username>/<string:password>/<string:device>/<string:start_time>/<string:end_time>/<string:volume>/')
def addevent(username, password, device, start_time, end_time, volume):
    login_code = manager.login_user(username, password);
    if login_code == constants.LOGIN_FAILED:
        return login_code;
        
    return manager.add_event(username, device, start_time, end_time, volume);
    
@cross_origin
@app.route('/geteventdata/<string:username>/<string:password>/<string:data_points>')
def get_event_data(username, password, data_points):
    login_code = manager.login_user(username, password);
    if login_code == constants.LOGIN_FAILED:
        return login_code;
        
    return manager.get_event_data(username, data_points);

@cross_origin
@app.route('/geteventdata/<string:username>/<string:password>/<string:device>/<string:data_points>')
def get_event_data_device(username, password, device, data_points):
    login_code = manager.login_user(username, password);
    if login_code == constants.LOGIN_FAILED:
        return login_code;
        
    return manager.get_event_data_device(username, device, data_points);
    
    
@cross_origin
@app.route('/lasttimevolume/<string:username>/<string:password>/<string:device>')
def last_time_volume(username, password, device):
    login_code = manager.login_user(username, password);
    if login_code == constants.LOGIN_FAILED:
        return login_code;
    
    return str(manager.get_last_time_volume(username, device));

@cross_origin
@app.route('/breakdown/<string:username>/<string:password>/<string:data_points>')
def breakdown(username, password, data_points):
    login_code = manager.login_user(username, password);
    if login_code == constants.LOGIN_FAILED:
        return login_code;
    
    return str(manager.get_breakdown(username, data_points));

@cross_origin
@app.route('/getlastevent/<string:username>/<string:password>')
def get_last_event(username, password):
    login_code = manager.login_user(username, password);
    if login_code == constants.LOGIN_FAILED:
        return login_code;
    
    return manager.get_last_event(username, password);

@cross_origin
@app.route('/gettodaysusage/<string:username>/<string:password>')
def get_todays_usage(username, password):
    login_code = manager.login_user(username, password);
    if login_code == constants.LOGIN_FAILED:
        return login_code;
    
    return manager.get_todays_usage(username, password);

@cross_origin
@app.route('/clear/<string:username>/<string:password>')
def clear(username, password):
    login_code = manager.login_user(username, password);
    if login_code == constants.LOGIN_SUCCESS and username == 'admin':
        manager.clear();
        return constants.CLEAR_SUCCESS;
        
    return constants.CLEAR_FAILED;

if __name__ == '__main__':
    app.run(host='0.0.0.0')