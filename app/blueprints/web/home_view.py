from app.blueprints.web import get_web_app

web = get_web_app()


@web.route('/', methods=['GET'])
def home():
    return "Hello World"
