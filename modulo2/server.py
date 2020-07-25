from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
#import mariadb
#conn = mariadb.connect(user="jorge.rios", password="Macros3", host="localhost", port=3306, database="proyectox")
#cur = conn.cursor()

#import sqlalchemy
#from sqlalchemy.orm import sessionmaker


# Test if it works
#engine = sqlalchemy.create_engine('mysql+mysqldb://jorge.rios:Macros3@localhost:3306/proyectox')
#conn = engine.connect().connection
#session= sessionmaker(bind =engine)()
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
#cors = CORS(app, resources={r"/auth": {"origins": "*"}})
#cors = CORS(app, resources={r"/*": {"origins": "*"}})
app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def main():
    #mariadbdriver
    #cur.execute("select nombre as nombre from personas")
    #headers = cur.description
    #vals = cur.fetchall()
    #for x in vals:
    #    print(x)

    #sqlalchemy
    #for x in session.execute("select nombre from personas"):
    #    print(x)

    
    return jsonify({"msg": "hola mundo"}), 200
    #return render_template('index.html')


@app.route('/usuario', methods=['GET'])
def usuario():
    if request.method == "POST":
        print(request.form)
    return render_template('index.html')




if __name__ == '__main__':
    app.run()

