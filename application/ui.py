from os import system
from typing import List
from util.color import Color


class UI(object):
    """ UI representa a interface do usuário.
    """

    @staticmethod
    def clear_screen() -> None:
        """ Limpa a tela do console.

        Returns:
            None
        """
        system("clear")

    @staticmethod
    def show_title() -> None:
        """ Mostra o título do jogo.

        Returns:
            None
        """
        print(f"{Color.COLOR_LIGHT_BLUE}### Seja bem vindo ao jogo da forca! ###{Color.RESET}\n")

    @staticmethod
    def show_category(category: str) -> None:
        """ Mostra a categoria selecionada.

        Returns:
            None
        """
        print(f'{Color.UNDERLINE}{Color.COLOR_GREEN}Localização{Color.RESET}{Color.COLOR_GREEN}: {category}{Color.RESET}')

    @staticmethod
    def show_lifes(lifes: List[str]) -> None:
        """ Mostra as vidas do jogador.

        Returns:
            None
        """
        print(f'{Color.UNDERLINE}{Color.COLOR_RED}Vidas{Color.RESET}{Color.COLOR_RED}: {" ".join(lifes)}{Color.RESET}')

    @staticmethod
    def show_hinted_words(hinted_words: List[str]) -> None:
        """ Mostra as letras já chutadas pelo jogador.

        Returns:
            None
        """
        print(f'{Color.UNDERLINE}{Color.COLOR_YELLOW}Letras já usadas{Color.RESET}{Color.COLOR_YELLOW}: {", ".join(hinted_words)}{Color.RESET}')

    @staticmethod
    def show_gallow(gallow_controller: int) -> None:
        """ Mostra o desenho da forca.

        Returns:
            None
        """
        GALLOWS_DISPLAY = [
            " _______"
            + "\n|"
            + "\n|"
            + "\n|"
            + "\n|"
            + "\n|"
            + "\n|", 
            " _______"
            + "\n|"
            + "\n|      😁"
            + "\n|"
            + "\n|"
            + "\n|"
            + "\n|",
            " _______"
            + "\n|"
            + "\n|      🤨"
            + "\n|      /|\\"
            + "\n|"
            + "\n|"
            + "\n|",
            " _______"
            + "\n|"
            + "\n|      😮"
            + "\n|      /|\\"
            + "\n|       |"
            + "\n|"
            + "\n|",
            " _______"
            + "\n|"
            + "\n|      😲"
            + "\n|      /|\\"
            + "\n|       |"
            + "\n|      / \\"
            + "\n|"
        ]
        print(f'{Color.COLOR_PURPLE}{GALLOWS_DISPLAY[gallow_controller]}{Color.RESET}\n')

    @staticmethod
    def show_underlines(underlines: List[str]) -> None:
        """ Mostra os campos a serem preenchidos pelo jogador.

        Returns:
            None
        """
        print(f'{Color.UNDERLINE}{Color.COLOR_DARK_BLUE}Palavra{Color.RESET}{Color.COLOR_DARK_BLUE}: {" ".join(underlines)}{Color.RESET}\n')

    @staticmethod
    def show_champion(word: str) -> None:
        """ Mostra uma mensagem de vitória e a palavra sorteada.

        Returns:
            None
        """
        print(f'{Color.COLOR_GREEN}Você venceu! A palavra sorteada foi: {word.upper()}{Color.RESET}\n')

    @staticmethod
    def show_loser(word: str) -> None:
        """ Mostra uma mensagem de derrota e a palavra sorteada.

        Returns:
            None
        """
        loser = " _______" \
            + "\n|"\
            + "\n|      💀" \
            + "\n|      /|\\" \
            + "\n|       |" \
            + "\n|      / \\" \
            + "\n|"

        print(f'{Color.COLOR_RED}{loser}')
        print(f'Você perdeu! A palavra sorteada foi: {word.upper()}{Color.RESET}\n')

