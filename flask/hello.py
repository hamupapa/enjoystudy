from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    s = "abc"
    lis = ["a1", "a2", "a3"]
    dic = {"name":"John", "age":24}
    bl = True
    
    # index.html を開く
    # 第2引数以降でHTMLにpythonの値を渡すことができる
    html = render_template('index.html', s=s, lis=lis, dic=dic, bl=bl)
    return html

if __name__ == "__main__":
    app.run(debug=True)
