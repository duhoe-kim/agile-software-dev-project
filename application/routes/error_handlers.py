from application import app

from flask import render_template, request

@app.errorhandler(400)
def bad_request(e):
    
    error_message = "bad request"
    error_code = "400"

    app.logger.error(f"{error_message}: {error_code}, route: {request.url}")

    return render_template("error_page.html",
                           error_message = error_message,
                           error_code = error_code)

@app.errorhandler(401)
def unauthorized(e):
    
    error_message = "unauthorized"
    error_code = "401"

    app.logger.error(f"{error_message}: {error_code}, route: {request.url}")

    return render_template("error_page.html",
                           error_message = error_message,
                           error_code = error_code)

@app.errorhandler(403)
def forbidden(e):
    
    error_message = "forbidden access"
    error_code = "403"

    app.logger.error(f"{error_message}: {error_code}, route: {request.url}")

    return render_template("error_page.html",
                           error_message = error_message,
                           error_code = error_code)

@app.errorhandler(404)
def not_found(e):

    error_message = "page not found"
    error_code = "404"

    app.logger.error(f"{error_message}: {error_code}, route: {request.url}")

    return render_template("error_page.html",
                           error_message = error_message,
                           error_code = error_code)

@app.errorhandler(405)
def method_not_allowed(e):

    error_message = "method not allowed"
    error_code = "405"

    app.logger.error(f"{error_message}: {error_code}, route: {request.url}")
    
    return render_template("error_page.html",
                           error_message = error_message,
                           error_code = error_code)

@app.errorhandler(406)
def not_acceptable(e):

    error_message = "not acceptable request"
    error_code = "406"

    app.logger.error(f"{error_message}: {error_code}, route: {request.url}")

    return render_template("error_page.html",
                           error_message = error_message,
                           error_code = error_code)

@app.errorhandler(408)
def request_timeout(e):

    error_message = "request timeout"
    error_code = "408"

    app.logger.error(f"{error_message}: {error_code}, route: {request.url}")

    return render_template("error_page.html",
                           error_message = error_message,
                           error_code = error_code)


@app.errorhandler(500)
def server_error(e):

    error_message = "server error"
    error_code = "500"

    app.logger.error(f"{error_message}: {error_code}, route: {request.url}")

    return render_template("error_page.html",
                           error_message = error_message,
                           error_code = error_code)