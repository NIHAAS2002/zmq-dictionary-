import zmq
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
shared_list = []
while True:
    print("server side view:",shared_list)
    request = socket.recv_json()
    if request["action"] == "add":
        shared_list.append(request["data"])
    elif request["action"] == "remove":
        if request["data"] in shared_list:
            shared_list.remove(request["data"])
    elif request["action"] == "update":
        if request["data"] in shared_list:
            index = shared_list.index(request["data"])
            shared_list[index]=request["update"]
    socket.send_json(shared_list)