from flask import Flask, render_template, request, redirect
import distance
import location
import logging
import database


app = Flask(__name__)


logging.basicConfig(
    level=logging.DEBUG,
    filename="mylog.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
)
logging.basicConfig(
    level=logging.WARNING,
    filename="mylog.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
)
logging.basicConfig(
    level=logging.ERROR,
    filename="mylog.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
)
logging.basicConfig(
    level=logging.CRITICAL,
    filename="mylog.log",
    format="%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == "POST":
        city = request.form['city']
        street = request.form['street']
        house = request.form['house']

        local = city + street + house
        try:
            try:
                coordinates = location.location(local)
                logging.info(coordinates)
                Lo1 = float(coordinates[0])
                La1 = float(coordinates[1])
            except:
                return "При вычислении координат ошибка"

            try:
                calculated = distance.create_lo_la(coordinates)
                logging.info(calculated)
            except:
                return "при вычислении расстояния ошибка"

            try:
                id = database.receiver(city, street, house, Lo1, La1, calculated)
            except:
                return "При записи в бд ошибка"
            return redirect('/calculated_distance/' + f"{id}")
        except:
            return "При вычислении произошли ошибки"
    else:
        return render_template("create-article.html")


@app.route('/calculated_distance')
def calculated_distance():
    computed = database.calculated()
    return render_template("calculated_distance.html", computed=computed)


@app.route('/calculated_distance/<int:id>')
def post_detail(id):
    post = database.calculated_id(id)
    logging.info(post)
    return render_template("calculated_distance.html", post=post)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/posts')
def posts():
    articles = database.calculated()
    return render_template("posts.html", articles=articles)


@app.route('/posts/<int:id>/delete')
def post_delete(id):
    try:
        database.delete_calculated(id)
        return redirect('/posts')
    except:
        return "При удалении статьи возникли ошибки"


if __name__ == "__main__":
    app.run(debug=True)
