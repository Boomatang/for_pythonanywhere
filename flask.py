import Flask

app = Flask(__name__)

app.secret_key = 'A0Zr98j/3yX R~XHH!jiugf0983oihuuiiubnhuuaior23yX R~XHH!jiugf098uhspuswfdsdN]LWX/,?RT'


@app.route('/', methods=['POST', 'GET'])
def home():
    return 'This is the new home'
