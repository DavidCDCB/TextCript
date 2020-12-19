#! /usr/bin/python3
# _*_ coding: utf8 _*_

from os import system as exc
from os import popen
import sys
import re
import time

TITLE = '''
 __           _       _       ___ _ _  
/ _\ ___ _ __(_)_ __ | |_    / _ (_) |_ 
\ \ / __| '__| | '_ \| __|  / /_\/ | __|
_\ \ (__| |  | | |_) | |_  / /_)\| | |_  
\__/\___|_|  |_| .__/ \__| \____/|_|\__|
               |_|              
'''
MENU = '''[0] Establecer usuario
[1] Crear etiqueta
[2] Crear cambio
[3] Comparar ramas
[4] Fusionar rama
[5] Ver historial y estado
[6] Subir rama local
[7] Ir a rama especifica
[8] Crear rama
[9] Ir a cambio especifico'''

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

index = -1


def main():
	limpiar()
	global index
	mostrar_menu("Key.down")
	while(True):
		with verificar_paquete().Listener(on_press=mostrar_menu) as listen:
			listen.join()
		acciones(str(index))
		mostrar_menu("")


def verificar_paquete():
	try:
		from pynput import keyboard as k
	except Exception as e:
		print("Intalando Paquete...")
		if(sys.platform.startswith('linux')):
			exc("sudo pip3 install pynput")
		else:
			exc("pip install pynput")
		from pynput import keyboard as k
	return k


def modificar_index(tecla):
	global index
	if(str(tecla) == "Key.up"):
		if(index <= 0):
			index = 9
		else:
			index-=1
	if(str(tecla) == "Key.down" ):
		if(index >= 10):
			index = 0
		else:
			index+=1


def obtener_entrada(msg=""):
	string = input(msg)
	entrada = ""
	corregida = False

	if(sys.platform.startswith('linux')):
		for c in string:
			if(re.search("[0-9]",c) and corregida == False):
				entrada += ""
			else:
				entrada += c
				corregida = True
		entrada = entrada.replace(chr(27)+chr(91)+"A","")
		entrada = entrada.replace(chr(27)+chr(91)+"B","")
		entrada = entrada.replace(chr(27)+chr(91)+"C","")
		return entrada
	else:
		return string


def mostrar_menu(tecla):
	global index
	caracter = str(tecla)
	if("'" in caracter):
		if(caracter.split("'")[1].isnumeric()):
			index = int(caracter.split("'")[1])
			return False

	if(tecla == "" or str(tecla) == "Key.down" or str(tecla) == "Key.up" or str(tecla) == "Key.right"):
		modificar_index(tecla)

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
			print("\n")
			seleccion(MENU,index)
			print("\nUsa las teclas de dirección o presiona el numero de la Opción")
			if(str(tecla) == "Key.right"):
				return False		
				

def limpiar():
	if(sys.platform.startswith('linux')):
		exc("clear")
	else:
		exc("cls")


def efecto(lista):
	for line in lista.split("\n"):
		if("]" in line):
			print(BCOLORS["WARNING"]+line[:3]+BCOLORS["OKGREEN"]+line[3:]+BCOLORS["ENDC"])
		else:
			print(BCOLORS["OKCYAN"]+line+BCOLORS["ENDC"])
		#time.sleep(0.05)

		
def seleccion(lista,indice):
	cadena = ""
	for i in range(len(lista.split("\n"))):
		if(i == indice):
			cadena += "->"+BCOLORS["WARNING"]+lista.split("\n")[i][:3]+BCOLORS["OKGREEN"]+lista.split("\n")[i][3:]+BCOLORS["ENDC"]+"\n"
		else:
			cadena += "  "+BCOLORS["ENDC"]+lista.split("\n")[i]+"\n"
	print(cadena)
		
		
def clone():
	repo = obtener_entrada("Link HTTPS del repositorio a clonar > ")
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
		nombre = obtener_entrada("Usuario > ")
		exc("git config --global user.name '"+str(nombre)+"'")
		correo = obtener_entrada("Correo > ")
		exc("git config --global user.email '"+str(correo)+"'")
		exc("git config --list")

	if(opt == "1"):
		exc("git tag")
		etiqueta = obtener_entrada("\nCrear versión > ")
		descripcion = obtener_entrada("\nDescripción > ")
		exc("git tag -a "+etiqueta+" -m '"+str(descripcion)+"'")

	if(opt == "2"):
		print("\nCambios a confirmar...\n")
		exc("git status -sb")
		message = obtener_entrada("\nDescripción del cambio > ")
		exc("git add .")
		exc('git commit -m "'+str(message)+'"')
		limpiar()
		exc("git log -3 --graph --decorate --all --abbrev-commit")
		obtener_entrada()

	if(opt == "3"):
		limpiar()
		exc("git fetch")
		exc("\ngit branch -v -a")
		ramaA = obtener_entrada("\nComparar rama: > ")
		ramaB = obtener_entrada("Con la rama: > ")
		if(sys.platform.startswith('linux')):
			exc("git difftool -y --tool=meld "+str(ramaA)+" "+str(ramaB))
		else:
			print("-> INGRESAR ':q' PARA SALIR DEL COMPARADOR")
			obtener_entrada()
			exc("git difftool -y "+str(ramaA)+" "+str(ramaB))

	if(opt == "4"):
		exc("git fetch")
		exc("\ngit branch -v -a")
		rama = obtener_entrada("Rama a traer > ")
		exc("git diff "+str(rama))
		exc("git merge "+str(rama))
		obtener_entrada()

	if(opt == "5"):
		exc("git fetch")
		limpiar()
		exc('git log --graph --pretty=format:"%C(cyan)%h%Creset -> %an -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)%Creset" --abbrev-commit')
		obtener_entrada()
		limpiar()
		print("\n Ramas:\n")
		exc("git branch -v")
		obtener_entrada()
		print("\n Modificaciones sin reportar: \n")
		exc("git status -s")
		obtener_entrada()

	if(opt == "6"):
		limpiar()
		exc("git fetch")
		exc("git branch -v")
		rama = obtener_entrada("Rama a subir > ")
		exc("git push origin "+rama)
		obtener_entrada()

	if(opt == "7"):
		print("\nRamas:\n")
		exc("git branch -v")
		idCommit = obtener_entrada("Nombre de Rama > ")
		exc("git checkout "+idCommit)
		obtener_entrada()

	if(opt == "8"):
		limpiar()
		rama = obtener_entrada("Nombre de rama > ")
		exc("git branch "+str(rama))
		exc("git checkout "+str(rama))
		exc("git branch -v")
		obtener_entrada()

	if(opt == "9"):
		exc("git reflog")
		commit = obtener_entrada("ID de Commit > ")
		respuesta = obtener_entrada("¿Conservar modificaciones? s/n > ")
		if(respuesta.lower() == "s"):
			exc("git reset "+commit+" --soft")
		elif(respuesta.lower() == "n"):
			exc("git reset "+commit+" --hard")
		else:
			print("Abortado")
			obtener_entrada()
		exc("git log -3 --graph --decorate --all --abbrev-commit")

	#Para corregir cagazo en un commit acabado de crear :D
	if(opt == "10"):
		exc("git add .")
		exc("git commit --amend")
		obtener_entrada()


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		exit()
    