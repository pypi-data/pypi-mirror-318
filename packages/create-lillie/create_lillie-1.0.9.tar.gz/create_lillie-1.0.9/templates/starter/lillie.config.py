from lilliepy import Importer, FileRouter, static

config = {
    "verbose": True
}

Importer("components")
static("assets")
FileRouter("pages", verbose=config["verbose"])