import zmq
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://10.113.7.22:5555")
while True:
    print("Press 1 to add an item to the shared list")
    print("Press 2 to remove an item from the shared list")
    print("Press 3 to update an item from the shared list")
    print("Press any other key to view the shared list")
    choice = input("Enter your choice: ")
    if choice == "1":
        item = input("Enter the item to add: ")
        request = {"action": "add", "data": item}
        socket.send_json(request)
    elif choice == "2":
        item = input("Enter the item to remove: ")
        request = {"action": "remove", "data": item}
        socket.send_json(request)
    elif choice=="3":
        item = input("Enter the item to update: ")
        update_item = input("enter the updated value:")
        request = {"action": "update", "data": item,"update": update_item}
        socket.send_json(request)
    else:
        request = {"action": "view"}
        socket.send_json(request)
    response = socket.recv_json()
    print(response)