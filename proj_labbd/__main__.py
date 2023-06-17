from proj_labbd import app

def main():
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)

if __name__ == "__main__":
    main()
