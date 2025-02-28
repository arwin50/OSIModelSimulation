import pickle
import json
import base64

class PhysicalLayer:
    def send(self, data):
        print("[Physical Layer] Sending data as bits:", data)
        bits = ''.join(format(byte, '08b') for byte in data)
        print("[Physical Layer] Encoded bits:", bits)
        return bits
    
    def receive(self, bits):
        print("[Physical Layer] Receiving bits:", bits)
        bytes_data = bytes(int(bits[i:i+8], 2) for i in range(0, len(bits), 8))
        print("[Physical Layer] Decoded bytes:", bytes_data)
        return bytes_data

class DataLinkLayer:
    def send(self, data, mac_address):
        print("[Data Link Layer] Encapsulating data in a frame with MAC address:", mac_address)
        frame = {'MAC': mac_address, 'Data': data}
        print("[Data Link Layer] Frame content:", frame)
        return pickle.dumps(frame)
    
    def receive(self, frame):
        print("[Data Link Layer] Extracting data from frame")
        frame = pickle.loads(frame)
        print("[Data Link Layer] Extracted Data:", frame['Data'])
        return frame['Data']

class NetworkLayer:
    def send(self, data, ip_address):
        print("[Network Layer] Adding IP address:", ip_address)
        packet = {'IP': ip_address, 'Data': data}
        print("[Network Layer] Packet content:", packet)
        return json.dumps(packet)
    
    def receive(self, packet):
        print("[Network Layer] Extracting data from packet")
        packet = json.loads(packet)
        print("[Network Layer] Extracted Data:", packet['Data'])
        return packet['Data']

class TransportLayer:
    def send(self, data, seq_num=0):
        print("[Transport Layer] Adding sequencing and error handling, Seq num:", seq_num)
        segment = {'Seq': seq_num, 'Data': data}
        print("[Transport Layer] Segment content:", segment)
        return json.dumps(segment)
    
    def receive(self, segment):
        print("[Transport Layer] Extracting data from segment")
        segment = json.loads(segment)
        print("[Transport Layer] Extracted Data:", segment['Data'])
        return segment['Data']

class SessionLayer:
    def send(self, data, session_id):
        print("[Session Layer] Managing connection state, Session ID:", session_id)
        session_packet = {'Session': session_id, 'Data': data}
        print("[Session Layer] Session packet content:", session_packet)
        return json.dumps(session_packet)
    
    def receive(self, session_packet):
        print("[Session Layer] Extracting session data")
        session_packet = json.loads(session_packet)
        print("[Session Layer] Extracted Data:", session_packet['Data'])
        return session_packet['Data']

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

class ApplicationLayer:
    def send(self, request):
        print("[Application Layer] Handling HTTP-like request:", request)
        response = f"HTTP/1.1 200 OK\nContent: {request}"
        print("[Application Layer] Response generated:", response)
        return response
    
    def receive(self, response):
        print("[Application Layer] Processing HTTP-like response:", response)
        return response.split('\n')[1]

def main():
    string = input("Enter your message!\n")
    app = ApplicationLayer()
    pres = PresentationLayer()
    sess = SessionLayer()
    trans = TransportLayer()
    net = NetworkLayer()
    data_link = DataLinkLayer()
    phys = PhysicalLayer()
    
    print("\n--- Sending Data ---")
    encoded_request = pres.send(string)
    session_data = sess.send(encoded_request, session_id=123)
    transport_data = trans.send(session_data, seq_num=1)
    network_data = net.send(transport_data, ip_address="192.168.1.1")
    data_link_frame = data_link.send(network_data, mac_address="00:1B:44:11:3A:B7")
    physical_bits = phys.send(data_link_frame)
    
    print("\n--- Receiving Data ---")
    received_data_link = phys.receive(physical_bits)
    received_network = data_link.receive(received_data_link)
    received_transport = net.receive(received_network)
    received_session = trans.receive(received_transport)
    received_presentation = sess.receive(received_session)
    response = pres.receive(received_presentation)
    final_response = app.send(response)
    
    print("\nFinal Response:")
    print(final_response)

if __name__ == "__main__":
    main()