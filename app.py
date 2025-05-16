from flask import Flask, render_template, request, redirect, url_for
import calendar
from datetime import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/<int:aasta>/<int:kuu>')
def index(aasta=None, kuu=None):
    now = datetime.now()

    if aasta is None or kuu is None:
        aasta = now.year
        kuu = now.month

    # Loome kalendri
    kal = calendar.Calendar()
    paevad = kal.monthdayscalendar(aasta, kuu)

    # Päevade lühendid
    paevade_nimed = ['E', 'T', 'K', 'N', 'R', 'L', 'P']

    return render_template(
        'index.html',
        paevad=paevad,
        paevade_nimed=paevade_nimed,
        kuu=kuu,
        aasta=aasta
    def eelmine_kuu(aasta, kuu):
    if kuu == 1:
        return aasta - 1, 12
    return aasta, kuu - 1

def jargmine_kuu(aasta, kuu):
    if kuu == 12:
        return aasta + 1, 1
    return aasta, kuu + 1