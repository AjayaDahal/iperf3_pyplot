# iperf3_pyplot
Plots graph for the output for iperf3
The format of the file could be either of this:

1. 
Test Runtime 120 seconds:     # this line could be somthing like is the test runtime
From EPC and ENB in NUC3[client] to UE in NUC2[server]  # this line is the title of the test
[ ID] Interval           Transfer     Bandwidth         # this line is the title of the table from the test
[  5]   0.00-1.00   sec  3.78 MBytes  31.7 Mbits/sec                  
[  5]   1.00-2.00   sec  4.10 MBytes  34.4 Mbits/sec                  
[  5]   2.00-3.00   sec  4.18 MBytes  35.1 Mbits/sec        

2. 
Test Runtime 120 seconds:
From UE in (NUC3[client] to EPC and ENB in NUC2[server])
ID      Interval              Transfer    Bitrate        Retr    Cwnd
[  5]   0.00-1.00   sec  5.08 MBytes  42.6 Mbits/sec    0    313 KBytes       
[  5]   1.00-2.00   sec  4.85 MBytes  40.7 Mbits/sec   15    314 KBytes       
[  5]   2.00-3.00   sec  4.35 MBytes  36.5 Mbits/sec    0    362 KBytes      
