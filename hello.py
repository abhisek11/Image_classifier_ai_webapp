from flask import Flask
from keras.models import load_model
from keras.applications.resnet50 import Resnet50

MODEL_PATH = 'models/your_model.h5'

model = Resnet50(weights='imagenet')

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/predict')
def upload():
	if request.method == 'POST':

		f= request.file['file']

		f.save(file_path)