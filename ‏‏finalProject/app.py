from flask import Flask, request, render_template
import backend_code
class Application:
    def __init__(self):
        pass

    app = Flask(__name__)

    @app.route('/')# loud the form to fill the properties
    def load(self):
        return render_template('home.html')

    @app.route('/replace-link/', methods=['POST', 'GET'])
    def replace(self): #active the function- rename_file when the user submit the properties
        if request.method == 'POST':
            oldName = request.form['oldName']
            newName = request.form['newName']
            path = request.form['path']
            backend_code.renameFile(path, oldName, newName)
            return render_template('success.html')
        return render_template('home.html')

    @app.route("/cancel-last-replace/", methods=['POST', 'GET'])
    def cancel_last_replace(self): #active the function- cancel_last_action when the user click on the button
        if request.method == 'POST':
            backend_code.cancel_last_action()
            return render_template('home.html')
        return render_template('success.html')

    @staticmethod
    def run_application():
        app.debug= True
        app.run()


app = Application()
if __name__ == '__main__':
    app.run_application()
