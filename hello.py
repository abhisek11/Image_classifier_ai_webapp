from flask import Flask
from keras.models import load_model
from keras.applications.resnet50 import Resnet50

MODEL_PATH = 'models/your_model.h5'

model = Resnet50(weights='imagenet')

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

def model_predict(image_path,model):

	img=image.load_img(image_path)
	x= image.img_to_array(img)
	preds = model.predict(x)

	return preds

@app.route('/predict')
def upload():
	if request.method == 'POST':

		f= request.file['file']

		f.save(file_path)

		preds = model_predict(file_path, model)

		pred_class = decode_predictions(preds,top=1)

		return pred_class