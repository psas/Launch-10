#!/usr/bin/env python
import struct

packet_header = struct.Struct('!L')
tag_header = struct.Struct('!4sHL')

message_types = {
    'SEQN': packet_header,

    # Crescent GPS
    'GPS\x01': struct.Struct("<BBH 3d 5f HH"),
    #'GPS\x02': struct.Struct("<LLHHHH"),
    #'GPS\x4C': struct.Struct("<dH8x 81L 15L 12L H"),
    #'GPS\x5E': struct.Struct("<10d LHHHhhh H"),
    #'GPS\x5F': struct.Struct("<HxxL 10L 10L 10L H"),
    #'GPS\x60': struct.Struct("<xxHd " + ''.join(("BBBB" for i in range(12))) + "12L 12d 12d H"),
    #'GPS\x61': struct.Struct("<L 4H 3L 2H H"),
    #'GPS\x62': struct.Struct("<" + ''.join(("HBBBBbB" for i in range(8))) + "BBxx H"),
    #'GPS\x63': struct.Struct("<BBHd" + ''.join(("8B b 3B H 5h" for i in range(12))) + "hH H"),

    #MPU1950
    'MPU9': struct.Struct("<7H"),

    #MPL3115A2
    'MPL3': struct.Struct("<2L"),

    #ADIS-IMU
    'ADIS': struct.Struct("<12h"),

	#ROLL
	'ROLL': struct.Struct("<HB"),
}

with open('log_2013.06.30_12-11-11', 'r') as f_in:

    while True:

        fourcc = f_in.read(4)
        if fourcc == 'SEQN':
            #print repr(f_in.read(6))
            seqn, =  struct.unpack('>L', f_in.read(4))
            #print seqn,
            continue
        timestamp_hi, timestamp_lo = struct.unpack('>HL', f_in.read(6))

        if fourcc == 'ADIS':
            length, = struct.unpack('<H', f_in.read(2))
        else:
            length, = struct.unpack('>H', f_in.read(2))
        body = f_in.read(length)
        timestamp = timestamp_hi << 32 | timestamp_lo
        decoder = message_types.get(fourcc)

        if fourcc == 'ADIS':
            print seqn,',', timestamp,',',
            values = decoder.unpack(body)
            mks = [0]*12
            mks[0] = values[0]
            mks[1] = values[1]
            mks[2] = values[2]
            mks[3] = values[3]
            mks[4] = values[4]/333.0
            mks[5] = values[5]/333.0
            mks[6] = values[6]/333.0
            for v in mks:
                print v,',',
            print ""

        #print fourcc, timestamp, length
