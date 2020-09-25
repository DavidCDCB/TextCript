#! /usr/bin/python3
#https://gist.github.com/dasdo/9ff71c5c0efa037441b6
#https://desarrolloweb.com/articulos/trabajar-ramas-git.html
#https://www.campusmvp.es/recursos/post/como-eliminar-el-ultimo-commit-de-git-en-el-repositorio-de-origen-p-ej-github.aspx
import os
import sys

def inicio():
	while(True):
		limpiar()
		print("\n __           _       _       ___ _ _  ") 
		print("/ _\ ___ _ __(_)_ __ | |_    / _ (_) |_ ")
		print("\ \ / __| '__| | '_ \| __|  / /_\/ | __|")
		print("_\ \ (__| |  | | |_) | |_  / /_)\| | |_  ")
		print("\__/\___|_|  |_| .__/ \__| \____/|_|\__|")
		print("               |_|              ")
		os.system("git config --get user.name")
		os.system("git config --get user.email")
		os.system("git config --get remote.origin.url")
		os.system("git branch")
		if(os.popen('git config --get remote.origin.url').read()==""):
			print("Sin repositorio, se debe clonar un proyecto.")
		print("\n")
		menu()

def limpiar():
	if(sys.platform.startswith('linux')):
		os.system("clear")
	else:
		os.system("cls")

def menu():
	print("[0] Establecer usuario")
	print("[1] Clonar proyecto")
	print("[2] Crear cambio")
	print("[3] Comparar Ramas")
	print("[4] Fusionar Rama")
	print("[5] Ver historial y estado")
	print("[6] Subir ramas locales")
	print("[7] Ir a Commit o Rama")
	print("[8] Crear rama")
	print("[9] Deshacer ultimo commit")		
	acciones(input("Opción > "))

def acciones(opt):
	limpiar()
	if(opt == "0"):
		nombre=input("Usuario > ")
		os.system("git config --global user.name '"+str(nombre)+"'")
		correo=input("Correo > ")
		os.system("git config --global user.email '"+str(correo)+"'")
		os.system("git config --list")

	if(opt == "1"):
		repo=input("Link HTTPS del Repositorio > ")
		os.system("git clone "+str(repo))
		if(sys.platform.startswith('linux')):
			os.system("mv scriptGit.py ./"+str(repo.split("/")[4].split(".")[0]))
		else:
			os.system("move scriptGit.py "+str(repo.split("/")[4].split(".")[0]))
		print("Script Movido!!!")
		time.sleep(5)
		exit()
		
	if(opt == "2"):
		print("\nCambios a confirmar...\n")
		os.system("git status -sb")
		message=input("\nDescripción del cambio > ")
		os.system("git add .")
		os.system("git commit -m '"+str(message)+"'")
		limpiar()
		os.system("git log -3 --graph --decorate --all --abbrev-commit")
		input()
			
	if(opt == "3"):
		limpiar()
		os.system("git fetch")
		ramas=input("Ramas a comparar > ")
		if(sys.platform.startswith('linux')):
			os.system("git difftool -y --tool=meld "+str(ramas))
		else:
			print("-> INGRESAR ':q' PARA SALIR DEL COMPARADOR")
			input()
			os.system("git difftool -y "+str(ramas))
		
	if(opt == "4"):
		os.system("git fetch")
		rama=input("Rama a traer > ")
		os.system("git merge "+str(rama))
		input()
		
	if(opt == "5"):
		os.system("git fetch")
		limpiar()
		os.system('git log --graph --pretty=format:"%C(cyan)%h%Creset -> %an -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)%Creset" --abbrev-commit')
		input()
		limpiar()
		print("\n Ramas:\n")
		os.system("git branch -v")
		input()
		print("\n Modificaciones sin reportar: \n")
		os.system("git status -s")
		input()
		
	if(opt == "6"):
		limpiar()
		os.system("git fetch")
		os.system("git push origin --all")
		input()

	if(opt == "7"):
		print("\nRamas:\n")
		os.system("git branch -v")
		idCommit=input("Id del Commit o Rama > ")
		os.system("git checkout "+idCommit)
		input()
		
	if(opt == "8"):
		limpiar()
		rama=input("Nombre de rama > ")
		os.system("git branch "+str(rama))
		os.system("git checkout "+str(rama))
		os.system("git branch -v")
		input()

	if(opt == "9"):
		respuesta=input("¿Conservar modificaciones? s/n > ")
		if( respuesta is "s"):
			os.system("git reset --soft HEAD^")
		else:
			os.system("git reset --hard HEAD^")
		
limpiar()
inicio()

