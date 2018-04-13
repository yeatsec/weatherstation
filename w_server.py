# weather server: listens for publisher

import sys
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

socket.connect("tcp://localhost:5556")
socket.setsockopt_string(zmq.SUBSCRIBE, 0) # 0 in place of a filter, not sure if this is ok

