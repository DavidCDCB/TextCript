#! /usr/bin/python3
import os
import sys
import time

def limpiar():
	if(sys.platform.startswith('linux')):
		os.system("clear")
	else:
		os.system("cls")

def menu():
	print("[0] Establecer usuario")
	print("[1] Clonar proyecto")
	print("[2] Reportar cambio")
	print("[3] Comparar Local vs Remoto")
	print("[4] Adquirir cambios remotos")
	print("[5] Ver estado e historial")
	print("[6] Subir cambios locales")
	print("[7] Ir a Commit determinado")
	print("[8] Cambio rapido")		
	acciones(input("Opción: "))

def acciones(opt):
	limpiar()
	if(opt is "0"):
		nombre=input("Usuario:")
		os.system("git config --global user.name '"+str(nombre)+"'")
		correo=input("Correo:")
		os.system("git config --global user.email '"+str(correo)+"'")
		os.system("git config --list")

	if(opt is "1"):
		repo=input("Link Repositorio:")
		os.system("git clone "+str(repo))
		if(sys.platform.startswith('linux')):
			os.system("mv scriptGit.py ./"+str(repo.split("/")[4].split(".")[0]))
		else:
			os.system("move scriptGit.py "+str(repo.split("/")[4].split(".")[0]))
		print("Script Movido!!!")
		time.sleep(5)
		exit()
		
	if(opt is "2"):
		message=input("Descripción de cambio:")
		os.system("git status -sb")
		os.system("git add .")
		os.system("git commit -m '"+str(message)+"'")
		os.system("git log --graph --oneline")
		
	if(opt is "3"):
		limpiar()
		os.system("git fetch")
		if(sys.platform.startswith('linux')):
			os.system("git difftool -y --tool=meld master origin/master")
		else:
			print("INGRESAR ':q' PARA SALIR DEL COMPARADOR")
			input()
			os.system("git difftool -y master origin/master")
		
	if(opt is "4"):
		os.system("git fetch")
		os.system("git merge")
		input()
		
	if(opt is "5"):
		if(sys.platform.startswith('linux')):
			os.system("git log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)%Creset' --abbrev-commit")
		else:
			os.system("git log --graph --decorate --all --abbrev-commit")
		os.system("git status")
		
	if(opt is "6"):
		os.system("git push origin --all")

	if(opt is "7"):
		os.system("git log --graph --oneline --decorate --all")
		idCommit=input("Id del Commit: ")
		os.system("git checkout "+idCommit)
		
	if(opt is "8"):
		os.system("git commit -am 'Cambio_rapido'")
		os.system("git push origin --all")
		
limpiar()

while(True):
	print("\n")
	print(" __           _       _       ___ _ _  ") 
	print("/ _\ ___ _ __(_)_ __ | |_    / _ (_) |_ ")
	print("\ \ / __| '__| | '_ \| __|  / /_\/ | __|")
	print("_\ \ (__| |  | | |_) | |_  / /_)\| | |_  ")
	print("\__/\___|_|  |_| .__/ \__| \____/|_|\__|")
	print("               |_|              ")
	os.system("git config --get user.name")
	os.system("git config --get user.email")
	os.system("git config --get remote.origin.url")
	if(os.popen('git config --get remote.origin.url').read()==""):
		print("Sin repositorio")
	print("\n")
	menu()
