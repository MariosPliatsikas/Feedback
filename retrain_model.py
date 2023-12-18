import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from joblib import load, dump
from sqlalchemy import create_engine

# Step 1: Load feedback data from the database
engine = create_engine('sqlite:////tmp/test.db')  # replace with your database URI
df = pd.read_sql('SELECT * FROM feedback', engine)

# Step 2: Preprocess the data
# This is a simplified example, you might need to do more complex preprocessing
df['feedback_clean'] = df['feedback'].str.lower()

# Step 3: Vectorize the feedback text
vectorizer = CountVectorizer()

# Step 4: Load the existing model
model = load('model.joblib')

# Create a pipeline that first vectorizes the text then applies the model
pipeline = Pipeline([('vectorizer', vectorizer), ('model', model)])

# Step 5: Retrain the model with the new data
# This assumes that df['user_id'] contains the labels for the feedback
pipeline.fit(df['feedback_clean'], df['user_id'])

# Step 6: Save the updated model
dump(pipeline, 'model.joblib')
