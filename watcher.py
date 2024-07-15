import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        filename = os.path.basename(event.src_path)
        if event.event_type == 'created':
            print(f"File {filename} has been created.")
        elif event.event_type == 'modified':
            print(f"File {filename} has been modified.")
        elif event.event_type == 'deleted':
            print(f"File {filename} has been deleted.")

if __name__ == "__main__":
    path = 'E:\\WorkPlace\\Programming_Language\\Python\\convert_asc'  # Change this to the directory you want to watch
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print(f"Watching directory '{path}' for changes...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

"""Full Path watcher
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        elif event.event_type == 'created':
            print(f"File {event.src_path.split('/')[-1]} has been created.")
        elif event.event_type == 'modified':
            print(f"File {event.src_path.split('/')[-1]} has been modified.")
        elif event.event_type == 'deleted':
            print(f"File {event.src_path.split('/')[-1]} has been deleted.")

if __name__ == "__main__":
    path = 'E:/WorkPlace/Programming_Language/Python/convert_asc'  # Change this to the directory you want to watch
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print(f"Watching directory '{path}' for changes...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
"""