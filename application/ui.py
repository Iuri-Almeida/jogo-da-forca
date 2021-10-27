from os import system


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
        print(f"### Seja bem vindo ao jogo da forca! ###\n")

    @staticmethod
    def show_category(category: str) -> None:
        """ Mostra a categoria selecionada.

        Returns:
            None
        """
        print(f'Localização: {category}')

    @staticmethod
    def show_lifes(lifes: list[str]) -> None:
        """ Mostra as vidas do jogador.

        Returns:
            None
        """
        print(f'Vidas: {" ".join(lifes)}')

    @staticmethod
    def show_hinted_words(hinted_words: list[str]) -> None:
        """ Mostra as letras já chutadas pelo jogador.

        Returns:
            None
        """
        print(f'Letras já usadas: {", ".join(hinted_words)}')

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
            + "\n|",
            " _______"
            + "\n|"
            + "\n|      💀"
            + "\n|      /|\\"
            + "\n|       |"
            + "\n|      / \\"
            + "\n|"
        ]
        print(GALLOWS_DISPLAY[gallow_controller])

    @staticmethod
    def show_underlines(underlines: list[str]) -> None:
        """ Mostra os campos a serem preenchidos pelo jogador.

        Returns:
            None
        """
        print(f'Palavra: {" ".join(underlines)}')

    @staticmethod
    def show_champion(word: str) -> None:
        """ Mostra uma mensagem de vitória e a palavra sorteada.

        Returns:
            None
        """
        print(f'Você venceu! A palavra sorteada foi: {word.upper()}')

    @staticmethod
    def show_loser(word: str) -> None:
        """ Mostra uma mensagem de derrota e a palavra sorteada.

        Returns:
            None
        """
        print(f'Você perdeu! A palavra sorteada foi: {word.upper()}')

