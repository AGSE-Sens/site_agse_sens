import os
from flask_frozen import Freezer
from application import create_app

app = create_app()
app.config.update(
    FREEZER_BASE_URL = "https://sens-agse.eu.org/",
    FREEZER_IGNORE_404_NOT_FOUND = True,
)

freezer = Freezer(app)

@freezer.register_generator
def page_url_generator():
    for d in [x[0][18:] for x in os.walk("application/pages/")][1:]:
        yield "page.show_page", {"name":d}

if __name__ == "__main__":
    freezer.freeze()

