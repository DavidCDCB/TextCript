#! /usr/bin/python3
# _*_ coding: utf8 _*_

from os import system as exc
from os import popen
import sys
import time

TITLE = '''
 __           _       _       ___ _ _  
/ _\ ___ _ __(_)_ __ | |_    / _ (_) |_ 
\ \ / __| '__| | '_ \| __|  / /_\/ | __|
_\ \ (__| |  | | |_) | |_  / /_)\| | |_  
\__/\___|_|  |_| .__/ \__| \____/|_|\__|
               |_|              
'''
MENU = '''
[0] Establecer usuario
[1] Crear etiqueta
[2] Crear cambio
[3] Comparar ramas
[4] Fusionar rama
[5] Ver historial y estado
[6] Subir rama local
[7] Ir a rama especifica
[8] Crear rama
[9] Ir a cambio especifico
'''
BCOLORS = {
    "HEADER": '\033[95m',
    "OKBLUE": '\033[94m',
    "OKCYAN": '\033[96m',
    "OKGREEN": '\033[92m',
    "WARNING": '\033[93m',
    "FAIL": '\033[91m',
    "ENDC": '\033[0m',
    "BOLD": '\033[1m',
    "UNDERLINE": '\033[4m'
}


def inicio():
	while(True):
		limpiar()
		efecto(TITLE)
		if(popen('git config --get remote.origin.url').read() == ""):
			print("\nSin repositorio, se debe usar el script en la raiz de un proyecto.")
			clone()
		else:
			exc("git config --get user.name")
			exc("git config --get user.email")
			exc("git config --get remote.origin.url")
			exc("git branch")
			efecto(MENU)
			acciones(input("Opción > "))


def limpiar():
	if(sys.platform.startswith('linux')):
		exc("clear")
	else:
		exc("cls")


def efecto(lista):
	for line in lista.split("\n"):
		if("]" in line):
			print(BCOLORS["WARNING"]+line[:3]+BCOLORS["OKGREEN"]+line[3:])
		else:
			print(BCOLORS["OKCYAN"]+line)
		time.sleep(0.05)


def clone():
	repo = input("Link HTTPS del repositorio a clonar > ")
	exc("git clone "+str(repo))
	if(sys.platform.startswith('linux')):
		exc("mv scriptGit.py ./"+str(repo.split("/")[4].split(".")[0]))
	else:
		exc("move scriptGit.py "+str(repo.split("/")[4].split(".")[0]))
	print("Script Movido!!!")
	time.sleep(5)
	exit()


def acciones(opt):
	limpiar()
	if(opt == "0"):
		nombre = input("Usuario > ")
		exc("git config --global user.name '"+str(nombre)+"'")
		correo = input("Correo > ")
		exc("git config --global user.email '"+str(correo)+"'")
		exc("git config --list")

	if(opt == "1"):
		exc("git tag")
		etiqueta = input("\nCrear versión > ")
		descripcion = input("\nDescripción > ")
		exc("git tag -a "+etiqueta+" -m '"+str(descripcion)+"'")

	if(opt == "2"):
		print("\nCambios a confirmar...\n")
		exc("git status -sb")
		message = input("\nDescripción del cambio > ")
		exc("git add .")
		exc('git commit -m "'+str(message)+'"')
		limpiar()
		exc("git log -3 --graph --decorate --all --abbrev-commit")
		input()

	if(opt == "3"):
		limpiar()
		exc("git fetch")
		exc("\ngit branch -v -a")
		ramaA = input("\nComparar rama: > ")
		ramaB = input("Con la rama: > ")
		if(sys.platform.startswith('linux')):
			exc("git difftool -y --tool=meld "+str(ramaA)+" "+str(ramaB))
		else:
			print("-> INGRESAR ':q' PARA SALIR DEL COMPARADOR")
			input()
			exc("git difftool -y "+str(ramaA)+" "+str(ramaB))

	if(opt == "4"):
		exc("git fetch")
		exc("\ngit branch -v -a")
		rama = input("Rama a traer > ")
		exc("git diff "+str(rama))
		exc("git merge "+str(rama))
		input()

	if(opt == "5"):
		exc("git fetch")
		limpiar()
		exc('git log --graph --pretty=format:"%C(cyan)%h%Creset -> %an -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)%Creset" --abbrev-commit')
		input()
		limpiar()
		print("\n Ramas:\n")
		exc("git branch -v")
		input()
		print("\n Modificaciones sin reportar: \n")
		exc("git status -s")
		input()

	if(opt == "6"):
		limpiar()
		exc("git fetch")
		exc("git branch -v")
		rama = input("Rama a subir > ")
		exc("git push origin "+rama)
		input()

	if(opt == "7"):
		print("\nRamas:\n")
		exc("git branch -v")
		idCommit = input("Nombre de Rama > ")
		exc("git checkout "+idCommit)
		input()

	if(opt == "8"):
		limpiar()
		rama = input("Nombre de rama > ")
		exc("git branch "+str(rama))
		exc("git checkout "+str(rama))
		exc("git branch -v")
		input()

	if(opt == "9"):
		exc("git reflog")
		commit = input("ID de Commit > ")
		respuesta = input("¿Conservar modificaciones? s/n > ")
		if(respuesta.lower() == "s"):
			exc("git reset "+commit+" --soft")
		elif(respuesta.lower() == "n"):
			exc("git reset "+commit+" --hard")
		else:
			print("Abortado")
			input()
		exc("git log -3 --graph --decorate --all --abbrev-commit")

	#Para corregir cagazo en un commit acabado de crear :D
	if(opt == "10"):
		exc("git add .")
		exc("git commit --amend")
		input()


def main():
	limpiar()
	inicio()


if __name__ == "__main__":
    main()
