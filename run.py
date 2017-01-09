from app import app
from werkzeug.contrib.fixers import ProxyFix

if __name__ == "__main__": 
	app.wsgi_app = ProxyFix(app.wsgi_app)
	app.run(debug = True)