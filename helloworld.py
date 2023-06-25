from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello'


# debug=True 表示可以当代买改动以后，可以自动重启。
app.run(debug=True)
# 在production中不要使用debug=True，可以像Angular中定义配置文件

# 指定ip地址
app.run(host='192.168.0.101', debug=True)
# 可以使用host='0.0.0.0'可以通过外网访问此地址
app.run(host='0.0.0.0', debug=True, port=81)
