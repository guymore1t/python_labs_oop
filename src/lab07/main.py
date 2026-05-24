import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab01'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab03'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab06'))

from app import TicketApp
from cli import run_cli

DATA_FILE = os.path.join(os.path.dirname(__file__), "tickets.json")

if __name__ == "__main__":
    app = TicketApp(DATA_FILE)
    run_cli(app)
    app.save_to_file()