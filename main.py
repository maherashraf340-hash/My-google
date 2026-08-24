from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

port = int(os.environ.get("PORT", 8000))

print(f"Server started on port {port}")
server = HTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler)
server.serve_forever()
