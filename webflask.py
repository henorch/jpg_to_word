from flask import Flask, request, jsonify, send_file
import os
from main import Converter



app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "Welcome": "You can convert anything here"
    })
    
@app.route("/upload", methods=["POST"])
def converted():
    if 'file' not in request.files:
        return jsonify({"error":"Please upload the file to convert"})
    
    file = request.files['file']
    if file.filename == "":
        return jsonify({"error": "you have uploaded an empty file"})
    
    filepath = os.path.join('uploads', file.filename)
   
    os.makedirs('uploads', exist_ok=True)
    file.save(filepath)
    
    try:
       converted = Converter(filepath)
       converted.save_to_word(output=f"{os.path.splitext(file.filename)[0]}.docx")
       return jsonify({
           "extract_text" : "Successfully"
       })
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
