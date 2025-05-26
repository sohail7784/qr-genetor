#qr code scanner where u can get qr code for the individual account,you can use it in real world
print("1.instagram 2.snapchat 3.telegram")
print("3.linkdin 4.email 6.youtube")
user=input("select options :")
if user=="instagram".lower():
    import qrcode
    import time
    instagram="https://www.instagram.com/invites/contact/?igsh=11chbbwmf8xkm&utm_content=3r5usjt"
    insta_gen=qrcode.make(instagram)
    insta_gen.save("qrcode1.png")
    print("generating...")
    time.sleep(3)
    print("insta qr generated")
elif user=="snapchat".lower():
    import qrcode
    import time 
    snapchat="https://www.snapchat.com/add/sohailll.07?share_id=WRVydnxCpik&locale=en-GB"
    snap_qr=qrcode.make(snapchat)
    snap_qr.save("qrcode1.png")
    print("generating")
    time.sleep(3)
    print("snap qr generated")
elif user=="linkdin".lower():
    import qrcode
    import time
    linkdin="https://www.linkedin.com/in/mohammed-sohail-8070b42a6?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"
    linkdin_qr=qrcode.make(linkdin)
    linkdin_qr.save("qrcode1.png")
    print("generating....")
    time.sleep(3)
    print("linkdin qr generated")
elif user=="email".lower():
    import qrcode
    import webbrowser
    import time
    email="sohailmohammed5425@gmail.com".lower()
    subject=input("")
    body=input("")
    mail_to=f"{email} subject={subject}&body={body}"
    email_qr=qrcode.make(mail_to)
    email_qr.save("ano_email.qr.png")
    print("generating")
    time.sleep(3)
    print("email qr generated")
    webbrowser.open(mail_to)
elif user=="youtube".lower():
    import qrcode
    import time
    youtube="https://www.youtube.com/"
    qr=qrcode.make(youtube)
    qr.save("qrcode1.png")
    print("generating...")
    time.sleep(3)
    print("youtube qr generated")
elif user=="telegram".lower():
    import qrcode
    import time
    telegram="https://telegram.org/dl"
    tele_qr=qrcode.make(telegram)
    tele_qr.save("qrcode1.png")
    print("generating...")
    time.sleep(3)
    print("telegram qr generated")
else:
    print("option invalid")