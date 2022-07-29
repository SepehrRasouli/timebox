""" Minimalistic timeboxing app."""
import argparse as arg
from CONFIG import pickle_database_name
from database import DatabaseManager
from show import Show
parser = arg.ArgumentParser()
parser.add_argument(
    "-c","--create",help="""Creates a database.
    You can change the database name in CONFIG.py
    """,action="store_true"
)
parser.add_argument(
    "-a","--add",help="""Adds a new entry.
    Usage: task_details,starts_at,interval. starts_at should be in %H:%M format.""",nargs=3
)
parser.add_argument(
    "-d","--delete",help="""Remove an entry.
    Usage: task_number""",nargs=1
)
parser.add_argument(
    "-s","--show",help="""Shows timeboxing entries.""",action="store_true"
)
args = parser.parse_args()
database_manager = DatabaseManager(pickle_database_name)
show = Show()
if args.create:
    database_manager.create_database()

if args.add:
   data = database_manager.read_data_from_database()
    data.append(args.add)
    database_manager.dump_data_to_database(data)

if args.delete:
    data = database_manager.read_data_from_database()
    data.pop(int(''.join(args.delete)))
    database_manager.dump_data_to_database(data)

if args.show:
    data = database_manager.read_data_from_database()
    show = Show()
    show.show(data)
