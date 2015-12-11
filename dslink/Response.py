class Response:
    def __init__(self, json):
        self.json = json
        self.rid = json["rid"]

    def get_stream(self):
        return self.json


class ListResponse(Response):
    def __init__(self, json, path):
        Response.__init__(self, json)
        self.path = path
        self.node = self.process(json["updates"])

    def process(self, update):
        from dslink.Node import RemoteNode
        node = RemoteNode(self.path.split("/")[-1], None)
        node.link = None
        node.from_serialized(update)
        return node
