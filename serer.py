class RemoteConrolServer:
    #listens to requessts
    def  __init__(self,ip,port):
        self.ip=ip
        self.port=port
    @staticmethod
    def echo(request_info):
        print(request_info)
    @staticmethod
    def handle_requests(request_name, request_info):
        match request_name:
            case echo:
                echo(request_info)
            case _:
                result="unknown"


