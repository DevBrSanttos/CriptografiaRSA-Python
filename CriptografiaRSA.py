from random import randrange

class criptografia:
    objCripto = {
        "msg": "",
        "msgCriptografada": "",
        "msgDescriptografada": "",
        "p": "",
        "q": "",
        "chavePublicaN": "",
        "chavePublicaE": "",
        "totiente_N": "",
        "chavePrivadaD": ""
    }

    def criptografar(self, msg):
        self.objCripto["msg"] = msg

        #gerar numeros primos
        self.objCripto["p"] = self.gerarPrimo()
        self.objCripto["q"] = self.gerarPrimo()

        #gerar chaves publicas e Calcular totiente de phi(n)
        self.objCripto["totiente_N"] = (self.objCripto["p"] - 1) * (self.objCripto["q"] - 1)
        self.objCripto["chavePublicaN"] = self.objCripto["p"] * self.objCripto["q"]
        self.objCripto["chavePublicaE"] = self.gerar_E()

        #gerar chave privada
        self.objCripto["chavePrivadaD"] = self.calcularChavePrivada()
        #criptografar msg
        self.objCripto["msgCriptografada"] = self.criptarMsg()


    def criptarMsg(self): #criptografar mensagem
        list = []
        for caracter in self.preCriptografarMsg():
            list.append((caracter ** self.objCripto["chavePublicaE"]) % self.objCripto["chavePublicaN"])
        return list

    def preCriptografarMsg(self): #transformar caracteres da msg em numeros de acordo com tabela ASC
        preCriptografia = []
        for caracter in self.objCripto["msg"]:
            preCriptografia.append(ord(caracter))
        return preCriptografia

    # Escolher número primo aleatorio entre 1 e 100
    def gerarPrimo(self):
        while True:
            primo = randrange(1, 100)
            divisoes = 0
            contador = 1
            while (contador <= primo):
                if (primo % contador == 0):
                    divisoes += 1
                contador += 1

            if (divisoes == 2):
                return primo

    # Gerar chave publica E
    def gerar_E(self):

        def mdc(n1, n2):
            while (n2 != 0):
                rest = n1 % n2
                n1 = n2
                n2 = rest
            return n1

        while True:
            e = randrange(2, self.objCripto["totiente_N"])
            if (mdc(self.objCripto["totiente_N"], e) == 1):
                return e

    def calcularChavePrivada(self):
        d = 0  # cria a variavel d
        while ((d * self.objCripto["chavePublicaE"]) % self.objCripto["totiente_N"] != 1):
            d += 1  # adiciona mais 1 em d
        return d

    # Descriptografar Mensagem
    def descriptografar(self):
        mensagem = ''
        for caracter in self.objCripto["msgCriptografada"]:
            mensagem += chr((caracter ** self.objCripto["chavePrivadaD"]) % self.objCripto["chavePublicaN"])
        return mensagem




#Teste
mensagem = criptografia()
mensagem.criptografar("Uma mensagem qualquer")
mensagem.descriptografar()
print("chaves publicas: ", (mensagem.objCripto["chavePublicaN"], mensagem.objCripto["chavePublicaE"]))
print("chave privada: ", mensagem.objCripto["chavePrivadaD"])
print("Mensagem criptografada:", mensagem.objCripto["msgCriptografada"])
print("Mensagem Descriptografada:", mensagem.descriptografar())
