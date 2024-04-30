from flask import Flask,render_template,redirect,url_for,session,request
app=Flask(__name__)

username="siva"
password="siva123@"

Student_list=[]

app.secret_key="chandran123"

# @app.route("/",methods=["GET","POST"])
# def home_fun():
# #    namelist=[{"name":"siva","age":25}]
#    return render_template("base.html")

def session_act():
    return username in session

@app.route("/", methods=["GET", "POST"])
def login_fun(): 
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]

        if name == username and password == password:
            session["username"] = name
            return redirect(url_for('table'))
        else:
            return "Invalid username or password"
    return render_template("index.html")

@app.route("/logout")
def logout_fun():
    session.pop("username",None)
    return redirect(url_for("login_fun"))

@app.route("/navbar/")
def navbar():
    return render_template("base.html")


@app.route("/table/", methods=["GET", "POST"])
def table():
    if request.method=="POST":
        new_dict={}
        new_dict["Name"]=request.form["Name"]
        new_dict["Age"]=request.form["Age"]
        new_dict["Roll_No"]=request.form["Roll_No"]
        Sub_1=request.form["Sub_1"]
        Sub_2=request.form["Sub_2"]
        Sub_3=request.form["Sub_3"]
        Sub_4=request.form["Sub_4"]
        Sub_5=request.form["Sub_5"]
        marks=[Sub_1,Sub_2,Sub_3,Sub_4,Sub_5]
        new_dict["Marks"]=marks
        Student_list.append(new_dict)
    return render_template("table.html", data=Student_list)

@app.route("/add/", methods=["GET", "POST"])
def home_fun():
    if request.method=="POST":
        new_dict={}
        new_dict["Name"]=request.form["Name"]
        new_dict["Age"]=request.form["Age"]
        new_dict["Roll_No"]=request.form["Roll_No"]
        Sub_1=request.form["Sub_1"]
        Sub_2=request.form["Sub_2"]
        Sub_3=request.form["Sub_3"]
        Sub_4=request.form["Sub_4"]
        Sub_5=request.form["Sub_5"]
        marks=[Sub_1,Sub_2,Sub_3,Sub_4,Sub_5]
        new_dict["Marks"]=marks
        Student_list.append(new_dict)
        return redirect(url_for("table"))
    return render_template("add.html", data=Student_list)


@app.route("/edit/<int:id>", methods=["GET", "POST"])  
def edit(id):
    if request.method == "POST":
        edit_dict = Student_list[id - 1]
        edit_dict["Name"] = request.form["Name"]
        edit_dict["Age"] = request.form["Age"]
        edit_dict["Roll_No"] = request.form["Roll_No"]  
        Sub_1 = request.form["Sub_1"]
        Sub_2 = request.form["Sub_2"]
        Sub_3 = request.form["Sub_3"]
        Sub_4 = request.form["Sub_4"]
        Sub_5 = request.form["Sub_5"]
        Marks = [Sub_1, Sub_2, Sub_3, Sub_4, Sub_5]
        edit_dict["Marks"] = Marks
        return redirect(url_for("table"))
    edit_list = Student_list[id - 1]
    return render_template("edit.html", form_data=edit_list)

@app.route("/delete/<string:id>",methods=["GET","POST"])
def del_fun(id):
    Student_list.pop(int(id)-1)
    return redirect(url_for("table"))

if __name__=="__main__":
   app.run(debug=True) 