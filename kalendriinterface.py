from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Näidisandmed (võid asendada andmebaasist tulevate andmetega)
    tabeli_andmed = [
        {"E": "-", "T": "-", "K": "-", "N": "-", "R": "-", "L": "-", "P": "-"},
        {"E": "-", "T": "-", "K": "-", "N": "-", "R": "-", "L": "-", "P": "-"},
        {"E": "-", "T": "-", "K": "-", "N": "-", "R": "-", "L": "-", "P": "-"},
        {"E": "-", "T": "-", "K": "-", "N": "-", "R": "-", "L": "-", "P": "-"},
        {"E": "-", "T": "-", "K": "-", "N": "-", "R": "-", "L": "-", "P": "-"}
    ]
    return render_template("index.html", andmed=tabeli_andmed)

if __name__ == '__main__':
    app.run(debug=True)
