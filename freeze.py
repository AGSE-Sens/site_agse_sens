from flask_frozen import Freezer
from application import create_app

freezer = Freezer(create_app())

if __name__ == "__main__":
    freezer.freeze()
