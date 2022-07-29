from rich import print
from rich.panel import Panel
from datetime import datetime,timedelta
class Show:

    @staticmethod
    def _error_handler(func):
        def handler(*args,**kwargs):
            try:
                return func(*args,**kwargs)
            except Exception as e:
                raise e
        return handler

    @_error_handler
    @staticmethod
    def calculate_end_time(entry):
        start = datetime.strptime(entry[1],"%H:%M")
        end = start + timedelta(minutes=int(entry[2]))
        return end

    @_error_handler
    @staticmethod
    def show(data):
        data = sorted(data,key=lambda x:x[1])
        for entry,index in enumerate(data):
            end_time = calculate_end_time(entry)
            print(
                Panel(
                    f"[bold green]{entry[0]}",
                    title=f"[bold red]{entry[1]} | [bold cyan]Task Number:{index}",
                    subtitle=f"[bold blue]{end_time.hour}:{end_time.minute} | {entry[2]}"
                ),"\n"
            )

