import random

LANGUAGES = {
    'en': {
        'options': ['rock', 'paper', 'scissors'],
        'play_again': 'Do you want to play again? (y/n) ',
        'invalid_option': 'Invalid option. Please try again!',
        'computer_choice': 'Computer chose {choice}.',
        'tie': "It's a tie!",
        'win': 'You win!',
        'lose': 'Computer wins!',
        'goodbye': 'C ya!'
    },
    'pt': {
        'options': ['pedra', 'papel', 'tesoura'],
        'play_again': 'Bora mais uma? (s/n) ',
        'invalid_option': 'Opção inválida. Escolhe de novo!',
        'computer_choice': 'O computador escolheu {choice}.',
        'tie': 'Eita, porra! Empatou.',
        'win': 'Aê, caralho! Você ganhou!',
        'lose': 'Perdeu, trouxa!',
        'goodbye': 'Flw, vlw!'
    }
}


def play_game(language):
    lang = LANGUAGES[language]
    options = lang['options']
    print(f"Vamos jogar Pedra, Papel, Tesoura!" if language == 'pt' else "Let's play Rock, Paper, Scissors!")
    
    while True:
        user_choice = input(f"Escolha sua arma: ") if language == 'pt' else input("Your weapon of choice: ")
        user_choice = user_choice.lower()
        
        if user_choice not in options:
            print(lang['invalid_option'])
            continue
        
        computer_choice = random.choice(options)
        print(lang['computer_choice'].format(choice=computer_choice.capitalize()))
        
        if user_choice == computer_choice:
            print(lang['tie'])
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print(lang['win'])
        else:
            print(lang['lose'])
        
        play_again = input(lang['play_again'])
        if play_again.lower() == 'n':
            print(lang['goodbye'])
            break


def main():
    language = input("Qual a linguagem? (en/pt) ")
    play_game(language)


if __name__ == '__main__':
    main()
