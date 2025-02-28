import pickle

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