from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db=SQLAlchemy(app)


class todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(200),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)



    def __repr__(self):
        return '<Task %r>' %self.id


@app.route('/',methods=['POST','GET'])


def index():
    if request.method=='Post':
        task_content=request.form['content']
        new_task=todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'Error in adding task'
    else:
        tasks=todo.query.order_by(todo.date_created).all()
        print(tasks)
        return render_template("index.html",tasks=tasks)

if __name__=="__main__":
    app.run(debug=True)