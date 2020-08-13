from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    html = """
    <h1>HELLO</h1>
    """
    return html


datas = [45.7, 45, 10, 70.8]


@app.route('/signal')
def signal():
    global datas
    datas.append(float(request.args.get("data")))
    return str(datas)


@app.route('/view')
def view():
    global datas
    labels = [i + 1 for i in range(len(datas))]

    ctx = {"title": "그래프",
           "labels": labels,
           "data": datas,
           }

    return render_template("view.html", ctx=ctx)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8000)
