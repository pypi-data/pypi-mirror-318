from lilliepy import component, html, link, use_CSS, use_Image, Favicon, Title

@component
def not_found():
    src = use_Image(media_file="icon.png", return_src=True).render()
    return html.div(
            {"id": "main"},
            Title("Oops"),
            Favicon(src),
            use_CSS("lost.css"),
            html.h1("OOPS,"),
            html.h2("Looks like you got lost"),
            link({"to": "/"}, "Click here to go back to the Homepage")
        )