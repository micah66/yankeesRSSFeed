from bottle import run, route, get, request, response
import bottle as b
import feedparser as f
import json
from sys import argv
script, filename = argv 


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
    refreshed = int(request.get_cookie('refresh_count', 0)) + 1
    response.set_cookie('refresh_count', str(refreshed), max_age=3600*24)
    get_feed_data = {
        'data': feed_list,
        'cookies': refreshed
    }
    return json.dumps(get_feed_data)


def main():
    run(host='0.0.0.0', port=argv[1])


if __name__ == '__main__':
    main()
