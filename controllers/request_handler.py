from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import urlparse
from services.user_service import UserService

class APIHandler(BaseHTTPRequestHandler):
    user_service = UserService()

    def send_json_response(self, status_code: int, payload: dict | list):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode("utf-8"))

    def get_body(self):
        try:
            content_length = int(self.headers.get("Content-Length", 0))
            if content_length == 0:
                return None
            body = self.rfile.read(content_length).decode("utf-8")
            return json.loads(body)
        except (json.JSONDecodeError, ValueError):
            return None

    def do_GET(self):
        parsed_url = urlparse(self.path)

        if parsed_url.path == "/api/users":
            status, response = self.user_service.get_users()
            self.send_json_response(
                status_code = status,
                payload = response
            )
        else:
            self.send_json_response(
                status_code = 404,
                payload = {"error": "Endpoint not found"}
            )

    def do_POST(self):
        parsed_url = urlparse(self.path)

        if parsed_url.path == "/api/users":
            body = self.get_body()

            if not body:
                self.send_json_response(
                    status_code = 400,
                    payload = {"error": "Invalid or missing body"}
                )
                return

            status, response = self.user_service.create_user(body)
            self.send_json_response(
                status_code = status,
                payload = response
            )

        else:
            self.send_json_response(
                status_code = 404,
                payload = {"error": "Endpoint not found"}
            )
