import asyncio
import http.server
import os
import socket
import threading
import websockets
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

DIRECTORY_TO_WATCH = "."  # The directory to watch for changes
PORT = 8000  # Port for HTTP server
WS_PORT = 8001  # Port for websocket server


class ChangeHandler(FileSystemEventHandler):
    def __init__(self, callback):
        self.callback = callback

    def on_any_event(self, event):
        if event.is_directory:
            return
        if event.event_type in ["created", "modified", "deleted"]:
            self.callback()


def serve_http():
    handler_class = http.server.SimpleHTTPRequestHandler
    httpd = http.server.HTTPServer(("localhost", PORT), handler_class)
    httpd.serve_forever()


def serve_websocket(clients):
    async def handler(websocket, path):
        clients.add(websocket)
        try:
            await websocket.wait_closed()
        finally:
            clients.remove(websocket)

    return websockets.serve(handler, "localhost", WS_PORT)


def start_watchdog(event_handler):
    observer = Observer()
    observer.schedule(event_handler, DIRECTORY_TO_WATCH, recursive=True)
    observer.start()
    observer.join()


# if __name__ == "__main__":
#     clients = set()

#     def notify_clients():
#         for ws in clients:
#             asyncio.run(ws.send("reload"))

#     event_handler = ChangeHandler(notify_clients)
#     threading.Thread(target=lambda: start_watchdog(event_handler), daemon=True).start()
#     threading.Thread(target=serve_http, daemon=True).start()

#     # loop = asyncio.get_event_loop()
#     loop = asyncio.get_running_loop()

#     loop.run_until_complete(serve_websocket(clients))
#     loop.run_forever()

if __name__ == "__main__":
    clients = set()

    def notify_clients():
        for ws in clients:
            asyncio.run(ws.send("reload"))

    event_handler = ChangeHandler(notify_clients)
    threading.Thread(target=lambda: start_watchdog(event_handler), daemon=True).start()
    threading.Thread(target=serve_http, daemon=True).start()

    # Correct way to handle event loop in modern Python versions
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(serve_websocket(clients))
    loop.run_forever()
