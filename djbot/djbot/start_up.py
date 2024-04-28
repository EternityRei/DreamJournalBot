from .api.commands.start_command import main
from dotenv import load_dotenv


def start_up():
    load_dotenv()
    main()
