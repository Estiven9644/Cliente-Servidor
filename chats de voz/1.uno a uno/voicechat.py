import pyaudio
import os
import zmq
import wave
import sys
import socket

def main():
    if len(sys.argv) != 3:
        print("Errooor!!!")
        exit()
    ip = sys.argv[1]
    port = sys.argv[2]
    context = zmq.Context()
    r = context.socket(zmq.REP)
    r.bind("tcp://*:8000")

    s = context.socket(zmq.REQ)
    s = connect("tcp://localhost:8000")


    CHUNK =  1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    #RECORD_SECONDS = 0.5

    p = pyaudio.PyAudio()

    receive_stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    send_stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)

    send_stream.start_stream()

    while True
        leer = receive_stream.read(chunk)
        s.send(leer)
        leer = r.recv(leer)
        send_stream.write(leer)
        r.send_string("escuchando")
        s.recv()

    receive_stream.stop_stream()
    receive_stream.close()
    send_stream.stop_stream()
    send_stream.close()

    p.terminate()

if __name__ == '__main__':
    main()
