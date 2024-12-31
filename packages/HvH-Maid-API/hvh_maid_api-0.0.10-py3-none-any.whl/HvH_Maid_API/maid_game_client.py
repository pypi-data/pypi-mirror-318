import socket
import time
import struct
from hashlib import sha256

import HvH_Maid_API
import HvH_Maid_API.byte_convertor as byte_bee
from HvH_Maid_API.messagebuf import MessageBuf
from HvH_Maid_API.authclient import AuthClient

from pathlib import Path

host = 'game.havenandhearth.com'
port = 1870
Server = {'msg_type':{0:'SESS',1:'REL',2:'ACK',3:'BEAT',6:'OBJDATA',7:'OBJACK',8:'CLOSE'}}


class MessageType(object):
    MSG_SESS = 0
    MSG_REL = 1
    MSG_ACK = 2
    MSG_BEAT = 3
    MSG_OBJDATA = 6
    MSG_OBJACK = 7
    MSG_CLOSE = 8

def combo_connect(login, passw, shizo_connect_number):
    acc_1 = AuthClient()
    my_hash = sha256(passw.encode('utf-8')).digest()
    passw_hash = sha256(passw.encode('utf-8')).hexdigest()
    passw_hash = my_hash

    script_location = Path(__file__).absolute().parent
    file_location = script_location / 'authsrv.crt'

    #acc_1.connect('game.havenandhearth.com', 1871, 'authsrv.crt')
    acc_1.connect('game.havenandhearth.com', 1871, file_location)
    cookie = acc_1.login(login, passw_hash)
    cookie_2 = cookie[5:]

    game_connect()
    print('game connected')
    game_start_session(login, cookie_2, shizo_connect_number)
    print('session started')
    

def game_connect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((host, port))
    Server['sock'] = sock

def game_start_session(username, cookie, shizo_connect_number):
        msg = MessageBuf()
        msg.add_uint8(MessageType.MSG_SESS)
        msg.add_uint16(2)
        msg.add_string('Hafen')
        msg.add_uint16(shizo_connect_number)
        msg.add_string(username)
        msg.add_uint16(len(cookie))
        msg.add_bytes(cookie)
        #print('Len:',len(cookie))
        #print('Len cookie:',len(cookie))
        #print('cookie:',cookie)
        game_send_msg(msg)
        
        #data = Server['sock'].recv(200)
        #dec = data.decode("utf-8")
        #print(data,' > ',dec),
        #print('AUTORIZATION MSG:', msg.buf)

        data, addr = Server['sock'].recvfrom(65535)
        print('data',data)

def receive_from_server():
    msg = {}
    msg['data'], msg['addr'] = Server['sock'].recvfrom(65535)
    msg['pos'] = 0
    msg['type'] = Server['msg_type'][byte_bee.get_uint8(msg)]
    msg['size'] = len(msg['data'])
    return msg

def find_sublist(sub, bigger):
    res = []
    if not bigger:
        return res
    if not sub:
        return 0
    first, rest = sub[0], sub[1:]
    pos = 0
    try:
        while True:
            pos = bigger.index(first, pos) + 1
            if not rest or bigger[pos:pos+len(rest)] == rest:
                #print('pp',pos)
                #return pos
                res.append(pos)
    except ValueError:
        #return -1
        return res

def send_3(wait):
    step = 0.1
    while wait >= 0:
        wait -= step
        send_msg_0([3])
        time.sleep(step)

def find_houses():
    count = 0
    acc_data = []
    houses = []
    while True:
        msg = receive_from_server()
        data = msg['data']
        data = list(data)
        acc_data += data
        print('-------', len(msg))
        res = find_sublist([21, 142, 1, 4], data)
        for aim in res:
            id_1 = []
            for i in reversed(range(0, 4)):
                id_1.append(data[aim - (21-2 + i)])
            #print(id_1)
            id_2 = []
            for i in reversed(range(0, 8)):
                id_2.append(data[aim - (8-2 + i)])
            #print(id_2)
            houses.append([id_1, id_2])

        count += 1
        if count > 20:
            break
        send_3(0.5)

    used_hashes = {}
    clean = []
    for el in houses:
        h = hash(str(el))
        if h not in used_hashes:
            used_hashes[h] = 1
            clean.append(el)
    houses = clean
    return houses

def open_doors(ids, n):
    signal = []
    signal += [1, n, 0, 1, 7, 0, 0, 0] #header?
    signal += [99, 108, 105, 99, 107, 0] #"click" keyword
    signal += [3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0]
    signal += [4, 3, 4, 0]
    signal += [4, 0, 1]
    signal += ids[0] #door id
    signal += [3]
    signal += ids[1] #door id               
    signal += [4, 0, 4, 16]

    send_msg_0(signal)
    

def text_to_bytes(text):
    text_b = []
    for el in text:
        b = bytes(el, 'utf-8')[0]
        text_b.append(b)
    return text_b
    

def chat_msg(text, shizo_number):
    b = text_to_bytes(text)
    msg = [1] + [shizo_number] + [0, 1, 24, 0, 0, 0, 109, 115, 103, 0, 2] + b + [0]
    send_msg_0(msg)

def char_select(name, shizo_number):
    b = text_to_bytes(name)
    msg = [1] + [shizo_number] + [0, 1, 3, 0, 0, 0, 112, 108, 97, 121, 0, 2] + b + [0]
    send_msg_0(msg)

def wow_im_so_so_smart_java_programmer():
    send_msg_0([1, 0, 0, 1, 0, 0, 0, 0, 102, 111, 99, 117, 115, 0, 1, 1, 0, 0, 0])

def hf_tp(shizo_number):
    #msg = [1] + [shizo_number] + [0, 1, 30, 0, 0, 0, 97, 99, 116, 0, 2, 116, 114, 97, 118, 101, 108, 0, 2, 104, 101, 97, 114, 116, 104, 0, 4, 0, 3, 8, 154, 241, 255, 130, 207, 240, 255]
    msg = [1] + [shizo_number] + [0, 1, 33, 0, 0, 0, 97, 99, 116, 0, 2, 116, 114, 97, 118, 101, 108, 0, 2, 104, 101, 97, 114, 116, 104, 0, 4, 0]
    send_msg_0(msg)

def switch_speed(speed, shizo_number): # 0,1,2,3
    #Send_msg_0([1, shizo_number, 0, 1, 28, 0, 0, 0, 115, 101, 116, 0, 4, speed])
    send_msg_0([1, shizo_number, 0, 1, 31, 0, 0, 0, 115, 101, 116, 0, 4, speed])
        
def send_to_server(msg):
    #print('MSG:',msg)
    Server['sock'].sendto(msg, (host, port))

def send_msg_0(b):
    msg = bytearray(b)
    send_to_server(msg)
    
def game_send_msg(msg):
    #print('MSG:',msg.buf)
    Server['sock'].sendto(msg.buf, (host, port))
