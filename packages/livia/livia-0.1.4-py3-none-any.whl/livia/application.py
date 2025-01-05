from cleo.application import Application
from cleo.commands.command import Command
from cleo.helpers import argument, option

from .chat import Chat


class ChatCommand(Command):
    name = "chat"
    description = "Chat with llm"
    options = [
        option(
            "model",
            description="model name",
            default=None,
            flag=False,
        ),
    ]

    def handle(self):
        model = self.option("model")
        chat = Chat()
        chat.chat_cli()


if __name__ == "__main__":

    application = Application()
    application.add(GreetCommand())
    application.run()
