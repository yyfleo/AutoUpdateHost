import socket, time, os, sys

domains=["www.google.com", "www.twitter.com", "www.facebook.com", "raw.githubusercontent.com"]

with open("hosts", "w") as f:
    f.write("# Updated On ")
    f.write(time.asctime(time.localtime(time.time())))
    f.write("\n# By yyfleo.\n")
    f.write("127.0.0.1 localhost\n::1 ip6-localhost\n")
    for domain in domains:
        if "https" in domain:
            domainInfo = socket.getaddrinfo(domain, 443)
        else:
            domainInfo = socket.getaddrinfo(domain, 80)
        f.write(domainInfo[0][4][0])
        f.write(" ")
        f.write(domain)
        f.write("\n")

os.system("dir")
os.system("ls")
os.system("ll")