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
def hello_world():
	return 'Hello World!'

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
