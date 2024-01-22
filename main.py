from flask import Flask, render_template, request, redirect
from steam import scrape

app = Flask('Game Scrapper')

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search')
def secondehome():
    fileName = request.args.get('fileName')
    if fileName == 'steam':
        games = scrape()
        return render_template('search.html', fileName = fileName, games = games)
    else:
        return redirect('/')

app.run()