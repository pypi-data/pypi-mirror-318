from lilliepy import component, html

@component
def home():
    return html._(
        html.h1("Home")
    )