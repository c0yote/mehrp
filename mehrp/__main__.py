import time

from mehrp import mehrp, mehrp_until_input

def main():
    print('Usage Demo:')

    print('Playing mehrp 3 times...\n')
    mehrp(3)

    time.sleep(.5)

    print('Playing until user input...')
    value = mehrp_until_input()
    print(f'Echoing input: {value}\n')
    
    time.sleep(.5)

    print('Playing until user input w/ prompt...')
    value = mehrp_until_input('> ')
    print(f'Echoing input: {value}\n')

if __name__ == '__main__':
    main()