import os
import csv

with open('./hosts.csv') as csvfile:
  reader = csv.reader(csvfile)
  for line in reader:
    for ip in line:
      response = os.system('ping -c 1 ' + str(ip))
      if response == 0:
          with open('./results.txt', 'a')as f:
              f.write("%s is up\n" % ip)
      else:
          with open('./results.txt', 'a')as f:
              f.write("%s is down\n" % ip)
