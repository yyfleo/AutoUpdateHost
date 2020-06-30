import socket, time, os

domains=["google.com", "twitter.com", "facebook.com", "youtube.com", "raw.githubusercontent.com", "instagram.com", "pixiv.net", "telegram.org", "steamcommunity.com", "logmein.com"]

if not os.path.exists("docs"):
    os.makedirs("docs")
with open("docs/hosts", "w") as f:
    f.write("# Updated On ")
    f.write(time.asctime(time.localtime(time.time())))
    f.write(" (UTC)\n# By yyfleo.\n")
    f.write("127.0.0.1 localhost\n::1 ip6-localhost\n")
    for domain in domains:
        print("Fetching the IP of " + domain)
        domainInfo = socket.getaddrinfo(domain, 443)
        f.write(domainInfo[0][4][0])
        f.write(" ")
        # if not len(domain.split(".")) == 2:
        #     temp = domain.split(".")
        #     domain = temp[len(temp) - 2] + "." + temp[len(temp) - 1]
        f.write(domain)
        f.write("\n")
