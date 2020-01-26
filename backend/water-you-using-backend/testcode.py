@app.route('/getdata/<string:username>/')
def getdata(username):
    return username

@app.route('/savestr/<string:filename>/<string:str>/')
def savestr(filename, str):
    data = [ { 'string' : str }, {'conststring' : 'constant'} ]
    json = demjson.encode(data)
    file = open(filename, "w")
    file.write(json)
    file.close()
    return 'File: ' + filename + ', String: ' + str

@app.route('/getstr/<string:filename>/')
def getstr(filename):
    #result = 'File not found'
    file = open(filename, "r")
    json = demjson.decode(file.read())
    
    #In the JSON object below, the statement below would return the text in str
    result = json[0].get('string')
    
    print('From manager: ' + manager.update_json_file(filename, json))
    file.close();
    return result