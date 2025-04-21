from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# وظيفة لفحص الموقع
def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return {"status": "success", "message": "Website is up and running!"}
        else:
            return {"status": "failure", "message": f"Website returned status code {response.status_code}"}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}

@app.route('/check', methods=['GET'])
def check():
    url = request.args.get('url')
    if not url:
        return jsonify({"status": "failure", "message": "URL parameter is missing"}), 400
    
    result = check_website(url)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
