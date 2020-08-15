from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'f106a85651d73990e22af513b9dbfa24'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Database Model
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_number = db.Column(db.String(6), unique=True, nullable=False)
    file_name = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return f"Group('{self.group_number}')"


# Creating dict from db data
def group_list():
    return {item.group_number: item.file_name for item in Group.query.all()}


# Route for home page
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/timetable/<group>')
def timetable_page(group):
    return render_template('timetable.html', title='Расписание', group=group)


@app.context_processor
def context_processor():
    return dict(group_list=[*group_list()])


if __name__ == '__main__':
    app.run(debug=True)
