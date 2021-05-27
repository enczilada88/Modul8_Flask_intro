from flask import Flask, render_template

app = Flask(__name__)

#mentor*********

@app.route("/mypage/me")
def mypage_me():
    return render_template("strona1.html")

@app.route("/mypage/contact")
def mypage_contact():
    return render_template("strona2.html")


#moje wewnętrzne
@app.route('/hello')
def hello():
    my_name = "Sylwia"
    return f'Hello Dear, {my_name}!'


@app.route('/blog/<id>')
def blog(id):
    return f"This is blog entry #{id}"


@app.route('/message_ugly', methods=['GET'])
def message_form_ugly():
    text = """
        <html>
            <head></head>

            <body>
                <form action="" method="POST">
                    <label>First Name</label>
                    <input name="firstname"/>
                    <input type="submit"/>
                </form>
            </body>
        </html  >
    """
    return text



@app.route("/warehouse_ugly")
def warehouse_ugly():
    items = ["screwdriver", "hammer", "saw"]
    html = "<ul>"
    for item in items:
        html = html + f"<li>{item}</li>"
    html += "</ul>"
    return html




from flask import render_template

@app.route('/messagee', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("form.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")


@app.route('/user/<name>')
def user(name):
    return render_template('form.html', name=name)

@app.route('/greetings')
def inforamtion():
    return render_template('greetings.html')


@app.route("/warehouse")
def warehouse():
    items = ["screwdriver", "hammer", "saw"]
    errors = ["hammer is broken!"]
    return render_template("warehouse.html", items=items, errors=errors)


@app.route("/warehouse_par")
def warehousepar():
    items = ["screwdriver", "hammer", "saw"]
    errors = ["hammer is broken!"]
    return render_template("parent.html", items=items, errors=errors)

@app.route("/warehouse_child1")
def warehousechild():
    items = ["screwdriver", "hammer", "saw"]
    errors = ["hammer is broken!"]
    return render_template("child1.html", items=items, errors=errors)



if __name__ == '__main__':
    app.run()