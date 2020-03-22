from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/') # routeはURLと関数を紐付けるためのもの
def index():
  s = "abc"
  lis = ["a1", "a2", "a3"]
  dic = {"name":"John", "age":24}
  bl = True
  
  # index.html を開く
  # 第2引数以降でHTMLにpythonの値を渡すことができる
  html = render_template('index.html', s=s, lis=lis, dic=dic, bl=bl)
  return html

# GET/POSTで値を渡す(requestのimportが必要)
@app.route('/test', methods=['GET', 'POST'])
def getpost():
  if request.method == 'GET':
    res = request.args.get('get_value')
  elif request.method == 'POST':
    res = request.form['post_value']
    
  return res
  
# GET/POSTで値を渡す 同じURLでもGETとPOSTで関数を分けることも可能
@app.route('/test2', methods=['GET'])
def get_test2():
  res = request.args.get('get_value2')
  return res

@app.route('/test2', methods=['POST'])
def post_test2():
  res = request.form['post_value2']
  return res

if __name__ == "__main__":
    app.run(debug=True)
