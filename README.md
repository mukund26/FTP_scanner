# FTP_scanner

FTP: The File Transfer Protocol (FTP) service allows users to transfer the ﬁles between hosts in a TCP-based network.
Typically, users authenticate to FTP servers using a combination of a username and password.

STEPS:-

So to build a FTP scanner with python module ftplib, one can follow these steps:-  

1.Construct a text ﬁle of a username/password combination that we want to brute force through.
2.Write a function bruteLogin() that take a host and password ﬁle path as input and return the credentials that allow access to the host. 
3.In bruteLogin(), the file is parsed for each combination of username and password and attempts to login to the FTP server.
4.If it succeeds, it returns a tuple of a username, password. 
5.If it fails, it passes through the exception and continues to the next line.
