#!/usr/bin/env python
import struct
import sys


packet_header = struct.Struct('!L')
tag_header = struct.Struct('!4sHLH')

message_types = {
    'SEQN': struct.Struct("<L"),
    #MPU1950
    'MPU9': struct.Struct("<7H"),
    #MPL3115A2
    'MPL3': struct.Struct("<2L"),
    #ADIS-IMU
    'ADIS': struct.Struct("<12h"),
	#ROLL
	'ROLL': struct.Struct("<HB"),
	#MESG
	'MESG': struct.Struct("sss"),

}


def adis2mks(unpack):
    mks = [0]*12
    mks[0] = unpack[0]          # Volatage
    mks[1] = unpack[1]          # X Gryro
    mks[2] = unpack[2]          # Y Gryro
    mks[3] = unpack[3]          # Z Gryro
    mks[4] = unpack[4]/333.0    # X Accel
    mks[5] = unpack[5]/333.0    # Y Accel
    mks[6] = unpack[6]/333.0    # Z Accel

    return mks


bytes_read = 0
with open(sys.argv[1], 'r') as source:

    while True:

        try:
            header = tag_header.unpack(source.read(tag_header.size))
            bytes_read += tag_header.size

            fourcc = header[0]
            timestamp = header[1] << 32 | header[2]
            length = header[3]
            #print fourcc, length


            body_struct = message_types[fourcc]
            body = body_struct.unpack(source.read(body_struct.size))
            bytes_read += body_struct.size

            if fourcc == "ADIS":
                print timestamp,',',repr(adis2mks(body))[1:-1]

        except:
            print "ERROR"
            print bytes_read
            break

print "end of file?"
print bytes_read

