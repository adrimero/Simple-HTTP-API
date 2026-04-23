from http.server import HTTPServer
from controllers.request_handler import APIHandler
from database import init_db

if __name__ == "__main__":
    init_db()
    port = 8000
    server = HTTPServer(("localhost", port), APIHandler)
    server.serve_forever()
