#coding=utf-8

from flask import Flask
import json
import random
import math
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)


@app.route('/')
def home_page():
	html = '''
	<html>
	<body>
	<a href="static/developer-map.html">developer-map </a><br>
	<a href="static/developer-map-brush.html">developer-map-brush </a><br>
	<a href="static/lines-airline.html">lines-airline </a><br>
	<a href="static/lines-airline-remote.html">lines-airline-remote </a><br>
	<a href="static/lines-bus.html"> lines-bus</a><br>
	<a href="static/pie-custom.html"> pie-custom</a><br>
	</body>
	</html>
	'''
	return html


@app.route('/json')
def gen_json():
	data = {'title': '访问来源-%s'%int(random.random()*20+2000),
			'data': [
			{'value': round(random.random()*200+100, 0), 'name':'直接访问'},
			{'value': round(random.random()*200+100, 0), 'name':'邮件营销'},
			{'value': round(random.random()*200+100, 0), 'name':'联盟广告'},
			{'value': round(random.random()*200+100, 0), 'name':'视频广告'},
			{'value': round(random.random()*200+100, 0), 'name':'搜索引擎'}]
			}
	return json.dumps(data)

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=888)
