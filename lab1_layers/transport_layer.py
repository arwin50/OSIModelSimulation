import json

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