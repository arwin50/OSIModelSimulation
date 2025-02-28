class ApplicationLayer:
    def send(self, request):
        print("[Application Layer] Handling HTTP-like request:", request)
        response = f"HTTP/1.1 200 OK\nContent: {request}"
        print("[Application Layer] Response generated:", response)
        return response
    
    def receive(self, response):
        print("[Application Layer] Processing HTTP-like response:", response)
        return response.split('\n')[1]