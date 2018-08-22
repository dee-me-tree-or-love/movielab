FLASK_APP = 'lookup/app.py'
FLASK_RUN_PORT = 8080


def get_start_command():
    app = FLASK_APP or 'lookup/app.py'
    port = FLASK_RUN_PORT or 8000
    command = (
        'export FLASK_APP={}' +
        ' && export FLASK_RUN_PORT={}' +
        ' && python -m flask run'
    ).format(app, port)

    return command
