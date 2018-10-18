from flask_api import FlaskAPI
from flask import request, url_for
from converter import *

app = FlaskAPI(__name__)


@app.route("/fetch", methods=['GET', 'POST'])
def data_list():
    """
    List or create notes.
    """
    err = 'sifanyi'
    read_CSV(file,json_file)
    output = read_json()
    return output



if __name__ == '__main__':
    app.run(debug=True)