from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):
    # print(url_for('static', filename='contrast_sun_adjust_ui_light_brightness_icon_251871.png'))
    return render_template('./index.html', name=username, post_id=post_id)


@app.route('/blog')
def blog():
    return 'These are my thoughts'


@app.route('/blog/2020')
def blog2():
    return 'These are my thoughts on 2020'


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# Save data in text file
def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


# Save data in CSV file
def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_write = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    # error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save your data!'
    else:
        return 'Something went wrong'
    # return render_template('login.html', error=error)
