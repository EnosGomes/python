from distutils.log import debug 
from fileinput import filename 
from flask import *  
import boto3
from flask_cors import CORS

app = Flask(__name__)  
cors = CORS(app, resources={r"/*": {"origins": "*"}}) 
s3 = boto3.client('s3')
  
# @app.route('/')   
# def main():   
#     return render_template("/index.html")   
# se for usar precisa criar uma pasta template e colocar todo o html la
  
@app.route('/success', methods = ['POST'])   
def success():   
    print("cheguei aqui")
    if request.method == 'POST':   
        f = request.files['file'] 
        f.save(f.filename)
        s3.upload_file('c:/Users/enos/Documents/pessoal/codigos/python/file.txt', 'bucket-enos', 'file.txt')
           
        return render_template("Acknowledgement.html", name = f.filename)   
  
if __name__ == '__main__':   
    app.run(debug=True)