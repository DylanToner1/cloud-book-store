from livereload import Server
from app import app

if __name__ == "__main__":
    app.debug = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    app.jinja_env.auto_reload = True

    server = Server(app.wsgi_app)

    server.watch("templates/**/*.html", delay=0.2)
    server.watch("static/css/*.css")
    server.serve(port=5001, host="0.0.0.0")
