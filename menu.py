import os
import getpass
password=getpass.getpass("Enter your password")
while password!='lw':
	print("enter the right password")
	password=getpass.getpass("Enter your password")
print("\t\t\t\t WELCOME TO MY MENU")
os.system("espeak-ng 'Welcome to my menu' ")
while True:
	os.system("sleep 4")
	os.system("clear")
	print("""
	\n
	press 1: to run date
	press 2 : to cal
	press 3 : to reboot
	press 4 : to user create
	press 5 : start webserver
	press 6 : check status of webserver.
	press 7 : to exit 
	press 8 : to activate the slave node
	press 9 : to activate the master
	press 10 : show the hadoop cluster
	press 11 : to start docker
	press 12 : to stop docker
	press 13 : check the status of docker
	press 14 : check the images available in docker
	press 15 : launch docker container
	press 16 : dowlaod new docker image  
        press 17 : to start jenkins
        press 18 : to stop jenkins
   
	""")

	

	r = input("enter your choice remote/local: ")

	ch = input("Enter ur choice : ")
	print(ch)
		

	if  r == "local" :
	 if int(ch) == 1:
	  os.system("date")
	 elif int(ch) == 2:
	  os.system("cal")
	 elif int(ch) == 3:
	  os.system("reboot")
	 elif int(ch) == 5:
	  os.system("systemctl start httpd")
	 elif int(ch) == 6:
	  os.system("systemctl status httpd")
	 elif int(ch) == 8:
	  os.system("hadoop-daemon.sh start datanode")
	  os.system("jps")
	  
	 elif int(ch) == 9:
	  print("please choose the remote login to configure master")

	 elif int(ch) == 10:
	  os.system("hadoop dfsadmin -report")
	 elif int(ch) == 11:
	  os.system("systemctl start docker")
	 elif int(ch) == 12:
	  os.system("systemctl stop docker")
	 elif int(ch) == 13:
	  os.system("systemctl status docker")
	 elif int(ch) == 14:
	  os.system("docker images")
	 elif int(ch) == 15:
	  img = input("Enter the image you want to launch : ")
	  ver = input("Enter the version you want to launch : ")
	  os.system("docker run -it {}:{}".format(img,ver))
	 elif int(ch) == 16:
	  img = input("Enter the image name : ")
	  ver = input("Enter the version : ")
	  os.system("docker run -it {}:{}".format(img,ver))
	 elif int(ch)==17:
	  os.system("systemctl start jenkins")
	 elif int(ch)==18:
	  os.system("systemctl stop jenkins")

		

	 elif int(ch) == 7:
	  exit()
	 else:
	  print("not supported")
	elif r == "remote":
	 ip=input("enter remote ip: ")
	 if int(ch) == 1:
	  os.system(" ssh {} date ". format(ip))
	 elif int(ch) ==2 :
	  os.system(" ssh {} cal". format(ip))
	 elif int(ch) == 3 : 
	  os.system(" ssh {} reboot" .  format(ip))
	 elif int(ch) == 5:
	  os.system("ssh {} systemctl start httpd" .format(ip))
	 elif int(ch) == 6:
	  os.system("ssh {} systemctl status httpd" .format(ip))
	 elif int(ch) ==8 :
	  print("this system is configures as data node , choose local login")
	 elif int(ch) ==9 :
	  os.system(" ssh {} hadoop-daemon.sh start namenode" . format(ip))
	  os.system(" ssh {} jps" . format(ip))

	 elif int(ch) == 10:
	  os.system("ssh {} hadoop dfsadmin -report". format(ip))
	 elif int(ch) == 11:
	  os.system("ssh {} systemctl start docker". format(ip))
	 elif int(ch) == 12:
	  os.system("ssh {} systemctl stop docker". format(ip))
	 elif int(ch) == 13:
	  os.system("ssh {} systemctl status docker". format(ip))
	 elif int(ch) == 14:
	  os.system("ssh {} docker images". format(ip))
	 elif int(ch) == 15:
	  img = input("Enter the image you want to launch : ")
	  ver = input("Enter the version you want to launch : ")
	  os.system("ssh {} docker run -it {}:{}".format(ip,img,ver))
	 elif int(ch) == 16:
	  img = input("Enter the image : ")
	  ver = input("Enter the version : ")
	  os.system("ssh {} docker run -it {}:{}".format(ip,img,ver))
	 elif int(ch)==17:
	  os.system("ssh {} systemctl start jenkins". format(ip))
	 elif int(ch)==18: 
	  os.system("ssh {} systemctl stop jenkins". format(ip))
	 
		

	 else:
	  print("not supported")
	else:
	 print("not supported login")
