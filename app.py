from flask import Flask, request, jsonify
from financial_analysis import generate_report
from data_preprocess import preprocess_data

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    """
    API endpoint to analyze financial data and generate a report.
    
    :return: JSON response with the generated financial report.
    """
    file_path = request.json['file_path']
    
    # Preprocess the financial data
    financial_data = preprocess_data(file_path)
    
    # Generate a financial report
    report = generate_report(financial_data)
    
    return jsonify({'report': report})

if __name__ == '__main__':
    app.run(debug=True)

