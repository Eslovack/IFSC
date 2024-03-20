import os

def cria(nomearquivo):
	try:
		comando =f"touch {nomearquivo}"
		retorno = os.system(comando)
		if retorno == 0:
			print(f"Arquivo {nomearquivo} criado")
		else:
			print(f"Falha ao criar o arquivo {nomearquivo}")
	except OSError as e:
		print(f"Erro ao tentar criar o arquivo {nomearquivo}: {e}")
if __name__ == "__main__":
    n = int(input("Digite o nome do arquivo: "))
    i = 0
    while (i <n):
	 nomearquivo = "arquivo"+str(i)+".txt"
	 cria(nomearquivo)
	 i+=1
