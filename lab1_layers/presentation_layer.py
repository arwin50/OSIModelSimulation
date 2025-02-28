import base64


class PresentationLayer:
    def send(self, data):
        print("[Presentation Layer] Encoding and compressing data:", data)
        encoded = base64.b64encode(data.encode()).decode()
        print("[Presentation Layer] Encoded Data:", encoded)
        return encoded
    
    def receive(self, encoded_data):
        print("[Presentation Layer] Decoding and decompressing data:", encoded_data)
        decoded = base64.b64decode(encoded_data.encode()).decode()
        print("[Presentation Layer] Decoded Data:", decoded)
        return decoded
