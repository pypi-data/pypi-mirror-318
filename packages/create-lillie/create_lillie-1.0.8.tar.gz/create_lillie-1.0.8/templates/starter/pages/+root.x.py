from lilliepy import component, html, Title, use_CSS, use_Image, Favicon

@component
def index():
    src = use_Image(media_file="icon.png", return_src=True).render()
    return html._(
        Title("Starter Lilliepy Page"),
        Favicon(src),
        use_CSS("css.css")
    )

@component
def img():
    return html.div(
        {"id": "img"},
        use_Image("image.png", "reactpy logo", False, {"id" : "img_content"})
    )

@component
def head():
    return html.div(
        {"id": "header"},
        html.h1("Welcome to ", html.a({'href': "https://lilliepy.pages.dev"},"Lillie.py!"))
    )

@component
def content():
    return html.div(
        {"id": "content"},
        html.p("edit this page in ",
               html.code("pages/+root.x.py"))
    )

def breaks(num):
    br = []
    for i in range(num):
        br.append(html.br())
    return br

@component
def root():
    return html._(
        index(),
        img(),
        *breaks(3),
        head(),
        content()
    )