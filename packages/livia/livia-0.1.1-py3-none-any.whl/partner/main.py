
from greet import GreetCommand

from cleo.application import Application


application = Application()
application.add(GreetCommand())

if __name__ == "__main__":
    application.run()