import http.server
import socketserver
from http.server import SimpleHTTPRequestHandler

class NoCacheHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

PORT = 8081
with socketserver.TCPServer(("", PORT), NoCacheHTTPRequestHandler) as httpd:
    print(f"Serveur démarré sur http://localhost:{PORT}")
    httpd.serve_forever()