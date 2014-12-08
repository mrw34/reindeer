#!/usr/bin/env python
import socket
import random
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.112.156.136', 8080))
data = s.recv(1024)
print data
s.send('Python\n')
while True:
  data = s.recv(1024)
  print data
  if data == 'WIN':
    break
  elif data == 'LOSE':
    break
  else:
    [N, E, S, W, P] = data.split()
    if P[1:] != '?':
      print 'P', P[1:]
      s.send(P[1:] + '\n')
    else:
      d = filter(lambda x: int(x[1:]), [N, E, S, W])
      random.shuffle(d)
      for _ in range(int(d[0][1:]) - 1):
        print d[0][0]
        s.send(d[0][0] + '\n')
        data = s.recv(1024)
        print data, '\n'
      print d[0][0]
      s.send(d[0][0] + '\n')
s.close()
