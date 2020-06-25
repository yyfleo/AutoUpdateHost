import socket, time, os

domains=["www.google.com", "www.twitter.com", "www.facebook.com", "www.youtube.com", "raw.githubusercontent.com"]

if not os.path.exists("docs"):
    os.makedirs("docs")
with open("docs/hosts", "w") as f:
    f.write("# Updated On ")
    f.write(time.asctime(time.localtime(time.time())))
    f.write(" (UTC)\n# By yyfleo.\n")
    f.write("127.0.0.1 localhost\n::1 ip6-localhost\n")
    for domain in domains:
        domainInfo = socket.getaddrinfo(domain, 443)
        f.write(domainInfo[0][4][0])
        f.write(" ")
        f.write(domain)
        f.write("\n")
