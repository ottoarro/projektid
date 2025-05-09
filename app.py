from flask import Flask, render_template
import calendar
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    aasta = datetime.now().year
    kuu = datetime.now().month

    # Loome kalendri
    kal = calendar.Calendar()
    paevad = kal.monthdayscalendar(aasta, kuu)

    # Päevade lühendid
    paevade_nimed = ['E', 'T', 'K', 'N', 'R', 'L', 'P']

    return render_template('index.html', paevad=paevad, paevade_nimed=paevade_nimed, kuu=kuu, aasta=aasta)

if __name__ == '__main__':
    app.run(debug=True)
