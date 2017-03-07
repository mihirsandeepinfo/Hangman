import random
def get_word():
    words = ['Woodstack','cars','Swayam','Mihir','bucket','lampost','apptitude','wall','aston','mercedes','wagonr','tesla','summer','winter','monsoon','raining','tortoise']
    return random.choice(words).upper()
def check(word,guesses,guess):
    status = ''
    matches = 0
    for letter in word:
        if letter in guesses:
            status+=letter
        else:
            status+='*'

        if letter==guess:
            matches+=1
    if matches>1:
        print('Yes, the word contains',matches,'"'+ guess +'"'+'s')
    elif matches ==1:
        print('Yes, the word contains the letter "'+guess+'"')
    else:
        print('Sorry, the word does not contain the letter "'+guess+'"')

    return status

def main():
    word = get_word()
    guesses = []
    guessed = False
    print('The word contains',len(word),'letters')
    while not guessed:
        text ='Please enter one letter or a {}-letter word. '.format(len(word))
        guess = input(text)
        guess = guess.upper()
        if guess in guesses:
            print('You already guessed "'+guess+'"')
        elif len(guess)== len(word):
            guesses.append(guess)
            if guess == word:
                guessed = True
            else:
                print('Sorry, that is incorrect')
        elif len(guess)==1:
            guesses.append(guess)
            result = check(word,guesses,guess)
            if result == word:
                guessed = True
            else:
                print(result)
        else:
            print('Invalid Entry')

    print('Yes, the word is ', word, '! You got it in ',len(guesses),'tries.')

main()





