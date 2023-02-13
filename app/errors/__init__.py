from flask import current_app, render_template
from app import limiter
import timeago, datetime

@current_app.errorhandler(404)
def page_not_found(e):
    return render_template("pages_error/404.html", code_status=404), 404

@current_app.errorhandler(429)
def too_many_requests(e):
    reset_at_date = datetime.datetime.fromtimestamp(limiter.current_limit.reset_at)
    reset_at = timeago.format(date=reset_at_date, locale="es")
    return render_template("pages_error/429.html", reset_at=reset_at, code_status=429), 429

