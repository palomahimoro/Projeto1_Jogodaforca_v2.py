#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Jogo da forca - versao 2


# In[ ]:


#import
import random
from os import system, name

#Funcao para limar a tela a cada execucao
def limpa_tela():
    #windows
    if name == 'nt':
        _ = system('cls')
        
    #Mac ou Linux
    else:
        _ = system('clear')
        
#Funcao que desenha a forca na tela
def display_hangman(chances):
    
    #lista de estagios da forca
    stages = [ # estagio 6 (final)
                """
                -------
                |     |
                |     O
                |    \\|/
                |     |
                |    / \\
                -
            """,
            # estagio 5
            """
                -------
                |     |
                |     O
                |    \\|/
                |     |
                |    /
                -
            """,
            # estagio 4
            """
                -------
                |     |
                |     O
                |    \\|/
                |     |
                |
                -
            """, 
            # estagio 3
            """    
                -------
                |     |
                |     O
                |    \\|/
                |     
                |    
                -
            """,
            # estagio 2
            """      
                -------
                |     |
                |     O
                |     |
                |     |
                |    
                -
                """,
            # estagio 1
            """      
                -------
                |     |
                |     O
                |     
                |     
                |    
                -
                """,
            # estagio 0
            """      
                -------
                |     |
                |     
                |     
                |     
                |    
                -
            """
    ]        
    return stages[chances]

#Funcao do jogo
def game():
    
    limpa_tela()
    print("\nBem vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")
    
    #Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    
    #escolhe randomicamente uma palavra
    palavra = random.choice(palavras)
    
    #lista de palavra da palavra
    lista_letras_palavras = [letra for letra in palavra]
    
    #cria o tabuleiro com caracter "-" multiplicado pelo comprimento da palavra
    tabuleiro = ["_"] * len(palavra)
    
    #numero de chances
    chances = 6
    
    #lista para as letras digitadas
    letras_tentativas = []
    
    #loop enquanto numero de chances for maior do que zero 
    while chances > 0:
        
        print(display_hangman(chances))
        print("Palavra: ", tabuleiro)
        print("\n")
        
        #tentativa
        tentativa = input("\nDigite uma letra: ")
        
        #condicional
        if tentativa in letras_tentativas:
            print("Voce ja tentou essa letra. Escolha outra!")
            continue
            
        #lista de tentativas(letras)
        letras_tentativas.append(tentativa)
        
        #condicional
        if tentativa in lista_letras_palavras:
            
            print("Voce acertou a letra!")
            
            #loop
            for indice in range(len(lista_letras_palavras)):
                
                #condicional
                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa
                    
            #se todos os espacos foram preenchidos, o jogo acabou
            if "_" not in tabuleiro:
                print("\nVoce venceu! A palavra era: {}".format(palavra))
                break
                
        else:
            print("Ops. Essa letra nao esta na palavra!")
            chances -=1
            
    #condicional
    if "_" in tabuleiro:
        print("\nVoce perdeu! A palavra era: {}.".format(palavra))
        
#Bloco main
if __name__ == "__main__":
    game()
    print("\nParabens. Voce esta aprendendo programacao.")


# In[4]:


[x**2 for x in range(1,11)]


# In[ ]:




