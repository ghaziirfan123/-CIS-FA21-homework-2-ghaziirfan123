from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from datetime import datetime

# creating flask app
app = Flask(__name__)

# configuring the database
app.config['MYSQL_HOST'] = 'homework-2.c9dwydo8r4pw.us-east-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'adminadmin'
app.config['MYSQL_DB'] = 'homework2'

# initialize MySQL app
mysql = MySQL(app)

'''
addcar adds a car to the database and logs the entry in the logs table
'''
@app.route('/api/addcar', methods=['POST'])
def addcar():
    content = request.json
    vin = content["vin"]
    make = content["make"]
    model = content["model"]
    year = content["year"]
    color = content["color"]
    username = content["username"]
    message = "Added car " + make + " " + model
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO `homework2`.`car` (`vin`, `make`, `model`, `year`, `color`) VALUES (%s,%s,%s,%s,%s)', (vin, make, model, year, color))
    cur.execute('INSERT INTO `homework2`.`logs` (`date`, `name`, `message`) VALUES (%s,%s,%s)', (datetime.now(), username, message))
    mysql.connection.commit()
    cur.close()
    return "OK", 200

'''
deletecar deletes a car from the database and logs the entry in the logs table
'''
@app.route('/api/deletecar', methods=['DELETE'])
def deletecar():
    content = request.json
    id = content["id"]
    username = content["username"]
    message = "Deleted car " + id
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM `homework2`.`car` WHERE id = %s', (id))
    cur.execute('INSERT INTO `homework2`.`logs` (`date`, `name`, `message`) VALUES (%s,%s,%s)', (datetime.now(), username, message))
    mysql.connection.commit()
    cur.close()
    return "OK", 200
    
'''
addmechanic adds a mechanic to the database and logs the entry in the logs table
'''
@app.route('/api/addmechanic', methods=['POST'])
def addmechanic():
    content = request.json
    firstname = content["firstname"]
    lastname = content["lastname"]
    title = content["title"]
    currentcar = content["currentcar"]
    username = content["username"]
    message = "Added Mechanic " + firstname + " " + lastname
    cur = mysql.connection.cursor()
    if currentcar == "":
        cur.execute('INSERT INTO `homework2`.`mechanic` (`firstname`, `lastname`, `title`) VALUES (%s,%s,%s)', (firstname, lastname, title))
    else:
        cur.execute('INSERT INTO `homework2`.`mechanic` (`firstname`, `lastname`, `title`, `currentcar`) VALUES (%s,%s,%s,%s)', (firstname, lastname, title, currentcar))
    cur.execute('INSERT INTO `homework2`.`logs` (`date`, `name`, `message`) VALUES (%s,%s,%s)', (datetime.now(), username, message))
    mysql.connection.commit()
    cur.close()
    return "OK", 200
    
'''
deletemechanic deletes a mechanic from the database and logs the entry in the logs table
'''
@app.route('/api/deletemechanic', methods=['DELETE'])
def deletemechanic():
    content = request.json
    id = content["id"]
    username = content["username"]
    message = "Deleted Mechanic " + id
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM `homework2`.`mechanic` WHERE id = %s', (id))
    cur.execute('INSERT INTO `homework2`.`logs` (`date`, `name`, `message`) VALUES (%s,%s,%s)', (datetime.now(), username, message))
    mysql.connection.commit()
    cur.close()
    return "OK", 200
    
'''
assigncar api assigns a car to a mechanic, only admin with specified password
can assigns a car. the task is also added to logs.
'''
@app.route('/api/assigncar', methods=['PUT'])
def assigncar():
    content = request.json
    username = content["username"]
    password = content["password"]
    if username == "admin" and password == "cars2000":
        id = content["id"]
        currentcar = content["currentcar"]
        message = "Assigned Car " + str(currentcar) + " Mechanic " + str(id)
        cur = mysql.connection.cursor()
        cur.execute('UPDATE `homework2`.`mechanic` SET currentcar = %s WHERE id = %s', (currentcar, id))
        cur.execute('INSERT INTO `homework2`.`logs` (`date`, `name`, `message`) VALUES (%s,%s,%s)', (datetime.now(), username, message))
        mysql.connection.commit()
        cur.close()
        return "OK", 200
    else:
        return "UNAUTHORIZED", 401

'''
unassigncar api unassigns a car from a mechanic, only admin with specified password
can unassign a car. the task is also added to logs.
'''
@app.route('/api/unassigncar', methods=['PUT'])
def unassigncar():
    content = request.json
    username = content["username"]
    password = content["password"]
    if username == "admin" and password == "cars2000":
        id = content["id"]
        currentcar = content["currentcar"]
        message = "Unassigned Car " + str(currentcar) + " Mechanic " + str(id)
        cur = mysql.connection.cursor()
        cur.execute('UPDATE `homework2`.`mechanic` SET currentcar = null WHERE id = %s and currentcar = %s', (id,currentcar))
        cur.execute('INSERT INTO `homework2`.`logs` (`date`, `name`, `message`) VALUES (%s,%s,%s)', (datetime.now(), username, message))
        mysql.connection.commit()
        cur.close()
        return "OK", 200
    else:
        return "UNAUTHORIZED", 401

'''
getlogs api returns the entries in the logs table and returns it as a string
'''
@app.route('/api/getlogs', methods=['GET'])
def getlogs():
    cur = mysql.connection.cursor()
    cur.execute('SELECT name, message, date from `homework2`.`logs`')
    string = ""
    for name, message, date in cur:
        string += name + " " + message + " " + str(date) + "<br>"
    cur.close()
    return string

# main driver code
if __name__ == '__main__':
    app.run(debug=True)
