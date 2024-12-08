from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os
import sys

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict the sentiment score for a given book review.
    
    Expects a JSON payload with 'title' and 'text' keys.
    """
    try:

        from data_preprocess import preprocess_data
        from predict import predict_sentiment

        # Parse the incoming JSON request
        data = request.json
        
        # Validate input
        if 'title' not in data or 'text' not in data:
            return jsonify({'error': 'Invalid input. JSON must include "title" and "text".'}), 400
        
        # Retrieve title and review for preprocessing
        input_data = pd.DataFrame([{
            'title': data['title'],
            'text': data['text']
        }])
        
        # Create texts merged column
        input_data['text_aug'] = input_data['title'] + " " + input_data['text']

        # Preprocess data
        processed_data = preprocess_data(input_data)
        
        # Extract the processed text for prediction
        text = processed_data['text_aug']
        
        # Predict using the pipeline
        scores, sentiments = predict_sentiment(text, pipeline)
        
        # Return the prediction as JSON
        return jsonify(
            {
                'score': float(scores[0]),
                'sentiment': sentiments[0]
            }
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Check if running inside Docker
running_in_docker = os.environ.get('RUNNING_IN_DOCKER', 'false') == 'true'
running_as_test = os.environ.get('RUNNING_AS_TEST', 'false') == 'true'

if running_in_docker:

    # Load the saved model pipeline from current directory in the container
    pipeline = joblib.load('model_pipeline.pkl')
    app.run()

else:

    sys.path.append("../scr/data")
    sys.path.append("../scr/models")

    # Load the saved pipeline from artifacts directory
    pipeline = joblib.load('../scr/models/artifacts/model_pipeline.pkl')

    if not running_as_test:
        app.run(debug=True)