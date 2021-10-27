"""
    Nome do projeto: Forca com POO
    Autor: Iuri Lopes Almeida
    Referências: https://github.com/Iuri-Almeida/letscode-webfullstack/blob/master/atividade-03/js/game.js
    Data: 27/10/2021
    Descrição: Jogo da Forca
    GitHub: https://github.com/Iuri-Almeida/jogo-da-forca
"""
from random import randint
from application.ui import UI
from unidecode import unidecode
from util.request import Api


def game(data):
    """ Realiza a lógica do jogo da forca.
    """
    # defining const variables
    WORD_NUMBER = randint(0, len(data) - 1)
    CATEGORY = data[WORD_NUMBER]['localizacao']['regiao']['nome']
    WORD = list(unidecode(data[WORD_NUMBER]['nome']['abreviado']).lower())
    
    # defining variables for gaming
    lifes = ['❤', '❤', '❤', '❤', '❤']
    display_controller = hits = 0
    hinted_words = []
    
    underlines = []
    for i in WORD:
        if i == ' ' or i == '-':
            underlines.append(i)
            hits += 1
        else:
            underlines.append('_')
    
    # Initializing game
    UI.clear_screen()
    UI.show_title()
    
    while lifes:

        UI.show_category(CATEGORY)
        UI.show_lifes(lifes)
        UI.show_hinted_words(hinted_words)
        UI.show_gallow(display_controller)
        UI.show_underlines(underlines)
        
        # getting user hint
        hint = ''
        while hint in hinted_words or len(hint) != 1 or not hint.isalpha():
            
            msg = ''
            
            if not hint:
                pass
            elif hint in hinted_words:
                msg = 'Esta letra já foi escolhida. '
            elif len(hint) != 1:
                msg = 'É preciso digitar somente uma única letra. '
            elif not hint.isalpha():
                msg = 'O que foi digitado não está no alfabeto. '

            hint = unidecode(input(f'{msg}Informe seu chute: ')).lower().strip()

        UI.clear_screen()

        hinted_words.append(hint)

        # check if it's one of the letter of the word
        if hint in WORD:
            for k, v in enumerate(WORD):
                if v == hint:
                    underlines[k] = v
                    hits += 1
        else:
            display_controller += 1
            lifes.pop()

        # victory
        if hits == len(WORD):
            UI.show_champion(''.join(WORD))
            break

    # defeat
    if len(lifes) == 0:
        UI.show_loser(''.join(WORD))


def main():

    api = Api('https://servicodados.ibge.gov.br/api/v1/paises/')
    
    # getting data
    data = api.get_data()
    
    # starting the game
    game(data)

    # play again
    while True:
        
        answer = input('Deseja jogar novamente? (s/n) ').strip().lower()
        while answer != 's' and answer != 'n':
            answer = input('Teste novamente. Deseja jogar novamente? (s/n) ').strip().lower()

        if answer == 's':
            game(data)
        else:
            break


if __name__ == '__main__':
    main()
