import os
import sys
import time

title='''
 __           _       _       ___ _ _  
/ _\ ___ _ __(_)_ __ | |_    / _ (_) |_ 
\ \ / __| '__| | '_ \| __|  / /_\/ | __|
_\ \ (__| |  | | |_) | |_  / /_)\| | |_  
\__/\___|_|  |_| .__/ \__| \____/|_|\__|
               |_|              
'''
menu='''
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
bcolors={
    "HEADER" : '\033[95m',
    "OKBLUE" : '\033[94m',
    "OKCYAN" : '\033[96m',
    "OKGREEN" : '\033[92m',
    "WARNING" : '\033[93m',
    "FAIL" : '\033[91m',
    "ENDC" : '\033[0m',
    "BOLD" : '\033[1m',
    "UNDERLINE" : '\033[4m'
}

def inicio():
	while(True):
		limpiar()
		efecto(title)
		if(os.popen('git config --get remote.origin.url').read()==""):
			print("\nSin repositorio, se debe usar el script en la raiz de un proyecto.")
			clone()
		else:
			os.system("git config --get user.name")
			os.system("git config --get user.email")
			os.system("git config --get remote.origin.url")
			os.system("git branch")
			efecto(menu)
			acciones(input("Opción > "))

def limpiar():
	if(sys.platform.startswith('linux')):
		os.system("clear")
	else:
		os.system("cls")

def efecto(lista):
	for line in lista.split("\n"):

		if("]" in line):
			print(bcolors["WARNING"]+line[:3]+bcolors["OKGREEN"]+line[3:])
		else:
			print(bcolors["OKCYAN"]+line)


def clone():
	repo=input("Link HTTPS del repositorio a clonar > ")
	os.system("git clone "+str(repo))
	if(sys.platform.startswith('linux')):
		os.system("mv scriptGit.py ./"+str(repo.split("/")[4].split(".")[0]))
	else:
		os.system("move scriptGit.py "+str(repo.split("/")[4].split(".")[0]))
	print("Script Movido!!!")
	time.sleep(5)
	exit()

def acciones(opt):
	limpiar()
	if(opt == "0"):
		nombre=input("Usuario > ")
		os.system("git config --global user.name '"+str(nombre)+"'")
		correo=input("Correo > ")
		os.system("git config --global user.email '"+str(correo)+"'")
		os.system("git config --list")

	if(opt == "1"):
		os.system("git tag")
		etiqueta=input("\nCrear versión > ")
		descripcion=input("\nDescripción > ")
		os.system("git tag -a "+etiqueta+" -m '"+str(descripcion)+"'")
		
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
		os.system("\ngit branch -v -a")
		ramaA=input("\nComparar rama: > ")
		ramaB=input("Con la rama: > ")
		if(sys.platform.startswith('linux')):
			os.system("git difftool -y --tool=meld "+str(ramaA)+" "+str(ramaB))
		else:
			print("-> INGRESAR ':q' PARA SALIR DEL COMPARADOR")
			input()
			os.system("git difftool -y "+str(ramaA)+" "+str(ramaB))
		
	if(opt == "4"):
		os.system("git fetch")
		os.system("\ngit branch -v -a")
		rama=input("Rama a traer > ")
		os.system("git diff "+str(rama))
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
		os.system("git branch -v")
		rama=input("Rama a subir > ")
		os.system("git push origin "+rama)
		input()

	if(opt == "7"):
		print("\nRamas:\n")
		os.system("git branch -v")
		idCommit=input("Nombre de Rama > ")
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
		os.system("git reflog")
		commit=input("ID de Commit > ")
		respuesta=input("¿Conservar modificaciones? s/n > ")
		if(respuesta.lower() == "s"):
			os.system("git reset "+commit+" --soft")
		elif(respuesta.lower() == "n"):
			os.system("git reset "+commit+" --hard")
		else:
			print("Abortado")
			input()
		os.system("git log -3 --graph --decorate --all --abbrev-commit")

	#Para corregir cagazo en un commit acabado de crear :D
	if(opt == "10"):
		os.system("git add .")
		os.system("git commit --amend")
		input()

def main():
	limpiar()
	inicio()

if __name__ == "__main__":
    main()
