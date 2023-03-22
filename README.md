# Rock, Paper, Scissors

[![License](https://img.shields.io/badge/license-GNU%20AGPLv3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

 A simple Python Rock, Paper, Scissors game.

## Table of Contents

- [Rock, Paper, Scissors](#rock-paper-scissors)
  - [Table of Contents](#table-of-contents)
  - [Why?](#why)
  - [How it works](#how-it-works)
  - [Contributing](#contributing)
  - [License](#license)

## Why?

Educational purposes and nothing more.

## How it works

This code imports the Python ```random``` module. It defines a dictionary called ```LANGUAGES```, which contains two sub-dictionaries, ```en``` and ```pt```, containing key-value pairs used for the messages displayed during the execution of the game. The keys of each sub-dictionary indicate the message to be displayed, while the values are the messages themselves. 


The ```play_game``` function receives a language parameter that is used to select the language for the messages. Inside the function, the game begins with a message prompt based on the selected language. 


The game will then ask the user for their choice of rock, paper or scissors, and the ```user_choice``` variable will store their response. If the user’s response is not one of the available options, an invalid_option message will be displayed prompting them to try again. 


If the user chooses a valid option, the computer will randomly select an option and display its choice. Then, by using a set of nested if statements, the function will evaluate whether the user wins, loses, or ties the round. Finally, the function asks if the user would like to play again. If not, the game ends. 


The ```main()``` function prompts the user to select a language and then begins the game. 


The execution of the code is protected by a standard Python condition checking if the program is being run as the main module.


## Contributing

Instructions on how to contribute to the project.

1. Fork the repository
2. Create a new branch (`git checkout -b feature/feature-name`)
3. Make your changes and commit them (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/feature-name`)
5. Create a new Pull Request

## License

This project is licensed under the [GNU AGPLv3 License](https://www.gnu.org/licenses/agpl-3.0).
