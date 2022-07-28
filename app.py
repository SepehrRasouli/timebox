import argsparse as arg
parser = arg.ArgumentParser()
parser.add_argument(
    "-a","--add",help="""Adds a new entry.
    Usage: task_details,starts_at,interval"""
)
parser.add_argument(
    "-d","--delete",help="""Remove an entry.
    Usage: task_number"""
)
parser.add_argument(
    "-s","--show",help="""Shows timeboxing entries."""
)
args = parser.parse_args()


