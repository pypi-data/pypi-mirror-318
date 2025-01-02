from lilliepy import Importer, FileRouter, static

Importer("components")
static("assets")
FileRouter("pages", verbose=True)