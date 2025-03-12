from flask import Flask, render_template, jsonify, send_from_directory
import json
import os

# Create the Flask application instance
app = Flask(__name__)

# Root route that renders the main dashboard page from the /templates folder
@app.route("/")
def index():
    return render_template("index.html")

# API endpoint to serve market share data from data/marketShare.json
@app.route("/api/marketShare")
def market_share():
    data_path = os.path.join(app.root_path, "data", "marketShare.json")
    with open(data_path, "r") as json_file:
        data = json.load(json_file)
    return jsonify(data)

# API endpoint to serve revenue trends data from data/revenueTrends.json
@app.route("/api/revenueTrends")
def revenue_trends():
    data_path = os.path.join(app.root_path, "data", "revenueTrends.json")
    with open(data_path, "r") as json_file:
        data = json.load(json_file)
    return jsonify(data)

# API endpoint to serve market segmentation data from data/marketSegmentation.json
@app.route("/api/marketSegmentation")
def market_segmentation():
    data_path = os.path.join(app.root_path, "data", "marketSegmentation.json")
    with open(data_path, "r") as json_file:
        data = json.load(json_file)
    return jsonify(data)

# Optional: Serve static files from the /static folder if needed.
# Flask automatically serves files from the /static folder, so you don't need an extra route unless customizing.

if __name__ == "__main__":
    # Enable debug mode for development; remove debug=True in production
    app.run(debug=True)
