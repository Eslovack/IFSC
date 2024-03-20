import os

def cria_pasta(nomepasta):
	try:
	     if not os.path.exists(nomepasta):
	            printf(f"A pasta {nomepasta} foi criada")
	     else:
		   printf(f"A pasra {nomepasta} JA EXISTE")
	except OSError as e:
	    print(f"Erro ao tentar criar {nomepasta}: {e}"
if __name__ == "__main__":
    nomepasta = input ("Digite o nome da pasta: ")
    cria_pasta(nomepasta)