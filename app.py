from flask import Flask, render_template

from main_folder.main import main_blueprint

app = Flask("app")

app.register_blueprint(main_blueprint)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('page404.html'), 404

@app.errorhandler(500)
def page_enternal(e):
    return render_template('page500.html'), 500

app.run(debug=True, host='0.0.0.0')

# if __name__ == "__main__":
#
#     app.run(debug=True, host='0.0.0.0')