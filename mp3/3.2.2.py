#!/usr/bin/python2.7
import dpkt
import sys
import socket


def main():
    if (len(sys.argv) < 2):
        print "error: need argument"
        # sys.exit(1)

    #filename = sys.argv[1]
    filename = "lbl-internal.20041004-1305.port002.dump.anon.pcap"
    #filename = "lbl-internal.20041004-1305.port002.dump.anon"
    #filename = '3.1.1.pcap'
    print "input filename: " + filename
    
    f = open(filename, 'rb')
    pcap = dpkt.pcap.Reader(f)
    
    #count = 0
    
    save_syn = {}
    save_syn_ack ={}

    
    for ts, buf in pcap:
        #print ts, len(buf)
        
#        print count
#        count += 1
        try: 
            eth = dpkt.ethernet.Ethernet(buf)
        except Exception:    
            #print "wrong parse!"
            continue
        
        if eth.type == dpkt.ethernet.ETH_TYPE_IP:
           
            ip = eth.data
        
            # if it's tcp packet
            if ip.p == dpkt.ip.IP_PROTO_TCP:
                #print "in if"
                tcp = ip.data
                
                src = socket.inet_ntoa(ip.src)
                dst = socket.inet_ntoa(ip.dst)
                
                #print "src: " + src + "dst: " + dst
                
                if tcp.flags & dpkt.tcp.TH_SYN != 0:
                    if tcp.flags & dpkt.tcp.TH_ACK != 0:
                        if ip not in save_syn_ack :
                            save_syn_ack[dst] = 0
                        save_syn_ack[dst] += 1
                    else:
                        if src not in save_syn :
                            save_syn[src] = 0
                        save_syn[src] += 1
                
                
            
    for adrs in save_syn:
        if adrs not in save_syn_ack:
            save_syn_ack[adrs] = 0
            if save_syn[adrs] > save_syn_ack[adrs] * 3:
                print adrs
    
    print "script finished!"
    #sys.exit(0)


if __name__ == '__main__':
    main()
