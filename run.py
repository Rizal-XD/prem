import os, re, sys, json,requests,time,marshal
if sys.version_info.major != 2:
	exit('\n\033[1;91mPlease use python 2 version\033[1;97m')

def clear(): # clear terminal
	if " linux" in sys.platform.lower():
		os.system("clear")
	elif "win" in sys.platform.lower():
		os.system("cls")
	else:os.system("clear")
if ("linux" in sys.platform.lower()):

        W = '\033[1;37m'
        N = '\033[0m'
        R = '\033[1;37m\033[31m'
        B = '\033[1;37m\033[34m'
        G = '\033[1;32m'
        O = '\033[1;37m\033[33m'
        C = '\033[36m'
        notice  = "{}{}[*]{} ".format(W,O,W)
        warning = "{}[#>]{} ".format(R,W)
        good    = "{}[!]{} ".format(G,N)
        warn    = "{}[!]{} ".format(O,N)
        line    = "\n"
else:

        W = ''
        N = ''
        R = ''
        B = ''
        G = ''
        O = ''
        C = ''
        notice  = ''
        warning = ''
        good=''
        d    = ''
        warn    = ''
        line    = ""
def banner():
	print("""{}      :::    :::              :::::::::  :::::::::   :::::::: {}
     :+:    :+:              :+:    :+: :+:    :+: :+:    :+: {}
     +:+  +:+               +:+    +:+ +:+    +:+ +:+    +:+  {}
     +#++:+  +{}#++:++#++:++ +#{}++:++#+  +#++:++#:  +#+    +:+   {}
   +#+  +#+               +#+        +#+    +#+ +#+    +#+    {}
 #+#    #+#              #+#        #+#    #+# #+#    #+#     {}
###    ###              ###        ###    ###  ########       {}{}{}\n
+#++:+  +#++:++#++:++ +#++:++#+  +#++:++#:  +#+    +:+
\t<\033[1;92mMASS BRUTE FACEBOOK COOKIE METHODE\033[1;97m>
{}CREATED BY\t : RIZAL XD
{}FACEBOOK\t : Muhamad Rizal Fiansyah Id
{}GITHUB \t : https://github.com/Rizal-XD
+#++:+  +#++:++#++:++ +#++:++#+  +#++:++#:  +#+    +:+""").format(R,G,B,O,G,C,C,R,G,B,W,line,notice,notice,notice)

while True:
	clear()
	banner()
	print '\n'
	print ' \t \t   [Select Methode Crack]'
	print '_________________________________________________________'
	print '  [ \033[1;92m01\033[1;97m ]  Crack With Graph Api ( \033[1;92mFaster!\033[1;97m,Kemungkinan Besar Result Chekpoint)'
	print '  [ \033[1;92m02\033[1;97m ]  Crack With M.Facebook ( \033[1;93mLambat \033[1;97m, Membutuhkan Koneksi Yang kuat ! Tetapi Result Cp kemungkinan Berkurang! )\n'
	try:
		choose = int(raw_input('\033[1;97mRizalXd />:\033[1;92m '))
	except ValueError:
		print('\n\033[1;91mHadeh\033[1;97m')
		exit()
	if choose == 1 or choose == 01:
		exec(marshal.loads('c\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00@\x00\x00\x00s\x11\x00\x00\x00e\x00\x00j\x01\x00d\x00\x00\x83\x01\x00\x01d\x01\x00S(\x02\x00\x00\x00s\x1a\x00\x00\x00python2 brute-cpython40.soN(\x02\x00\x00\x00t\x02\x00\x00\x00ost\x06\x00\x00\x00system(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00<roy>t\x08\x00\x00\x00<module>\x01\x00\x00\x00t\x00\x00\x00\x00'))
		exit()
	elif choose == 2 or choose == 02:
		print ('Jangan lupa donasi seiklashnya :"v')
		time.sleep(1)
		exec(marshal.loads('c\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00@\x00\x00\x00s\x11\x00\x00\x00e\x00\x00j\x01\x00d\x00\x00\x83\x01\x00\x01d\x01\x00S(\x02\x00\x00\x00s\x1a\x00\x00\x00python2 brute-cpython39.soN(\x02\x00\x00\x00t\x02\x00\x00\x00ost\x06\x00\x00\x00system(\x00\x00\x00\x00(\x00\x00\x00\x00(\x00\x00\x00\x00s\x05\x00\x00\x00<roy>t\x08\x00\x00\x00<module>\x01\x00\x00\x00t\x00\x00\x00\x00'))
		exit()
	else:
		print(R+"ISI YANG BENER"+W)
		