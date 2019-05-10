from flask import Flask, render_template, send_from_directory, jsonify, request
#from requests import  request






app = Flask(__name__)





@app.route('/index')
def index():
    return render_template('index.html', title='Zamow jedzenie')

@app.route('/output', methods=['POST'])
def output():

    print(request.get_json())

    return jsonify({'status': 'success'}), 201














if __name__ == '__main__':
   app.run(debug = True)

