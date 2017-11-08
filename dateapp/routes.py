from . import app
import datetime
from flask import request, render_template
from datetime import datetime


@app.route('/', methods=['GET'])
def home():
	if request.method == 'GET':
		day = request.args.get('date')
		if day:
			date_object = datetime.strptime(day, '%Y-%m-%d')
			date_return = date_object.strftime('%A, %B %d, %Y')
			return render_template('index.html', result=date_return)

		else:
			return render_template('index.html')