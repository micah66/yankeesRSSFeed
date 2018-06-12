from bottle import run, route, get
import bottle as b
import feedparser as f
import json


@route('/')
def index():
    return b.template('star1.html')


@route('/<filepath>')
def javascripts(filepath):
    return b.static_file(filepath, root='./')


@route('/https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js')
def jquery():
    return b.static_file('https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js')


@route('/<filepath>')
def stylesheet(filepath):
    return b.static_file(filepath, root='./')


@get('/get_feed')
def get_feed():

    feed = f.parse('http://mlb.mlb.com/partnerxml/gen/news/rss/nyy.xml')
    feed_list = [i for i in feed['entries'] if i['link']]
    return json.dumps(feed_list)


def main():
    run(host='localhost', port='7000', reloader=True)


if __name__ == '__main__':
    main()
