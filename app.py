from flask import render_template, request, Flask, send_file, send_from_directory
from PIL import Image

import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/img/<path:path>')
def send_js(path):
    return send_from_directory('./statics', path)

@app.route("/rec", methods = ['POST'])
def recg():
	f = request.files['file']
	fname = ''.join(random.choice("weui238uj89fwh9sfhiosdjfisdn89f2023jerio290u") for i in range(5))
	f.save('./statics/' + fname + '.gif')

	print("@@@", fname)

	#img = Image.open(request.files['file'].stream)

	#r = util.Recognizing('./statics/' + fname + '.gif')
	return str("<script>setTimeout(function(){document.getElementById('click').style['display'] = 'inline';}, 900);</script>"+\
	"<h1>第二步<br>计算中 ... </h1><br>"+\
	"<div id='click' style='display: none;'><a href='http://zheye.shidaixin.com/img/" + fname + ".gif'><h1>click me!</h1></a><br>"+\
	"<h1>打开图片,猜对了就给我一颗星吧 <a href='https://github.com/muchrooms/zheye'>github</a></h1></div>")
	


if __name__ == "__main__":
    app.run(debug=False)
