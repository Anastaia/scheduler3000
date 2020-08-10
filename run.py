from flask import Flask, render_template, url_for


app = Flask(__name__)


group_list = {
        '11-312': '312.pdf',
        '11-666': '666.pdf',
        '11-1337': '1337.pdf',
        '11-69': '69.pdf',
    }


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/timetable/<group>')
def timetable_page(group):
    return render_template('timetable.html', title='Расписание', group=group)


@app.context_processor
def context_processor():
    return dict(group_list=[*group_list])


if __name__ == '__main__':
    app.run(debug=True)
