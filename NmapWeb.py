import subprocess

sonuc=""
while 1:
    sonuc=subprocess.check_output("ngrep -d lo -n 1 port 80|grep /anasayfa.html",shell=True)
    try:
        subprocess.call("rm -rf /home/toor/PycharmProjects/calismalar/python.html")
    except:
        pass
    dosya=open("/home/toor/PycharmProjects/calismalar/python.html","a")
    dosya.write("<html>")
    dosya.write("<head>")
    dosya.write("<title>Gelen Istek</title>")
    dosya.write("</head>")
    dosya.write("<body>")
    yazi="<h1>"+str(sonuc)+"</h1>"
    dosya.write(yazi)
    dosya.write("</body>")
    dosya.write("</html>")
    dosya.close()
    subprocess.call("iceweasel /home/toor/PycharmProjects/calismalar/python.html",shell=True)
