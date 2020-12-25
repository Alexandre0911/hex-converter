import pyconverter



def encoding():
    decoded_text = input('\nPaste here the text: ')
    encoded_text = pyconverter.utf8tohex(decoded_text)
    print('\nEncoded text: {}'.format(encoded_text))

def decoding():
    encoded_text = input('\nPaste here the text: ')
    decoded_text = pyconverter.hextoutf8(encoded_text)
    print('\nDecoded text: {}'.format(decoded_text))



def link():
    decoded_text = input('\nPaste here the text: ')
    decoded_text_list = []
    for c in range(len(decoded_text)):
        if c % 2 == 0:
            decoded_text_list.append('%')
            decoded_text_list.append(decoded_text[c])
        elif c % 2 != 0:
            decoded_text_list.append(decoded_text[c])
    encoded_text = pyconverter.utf8tohex(decoded_text)
    print('\nLink: "http://google.com/search?btnI&q={}"'.format(encoded_text))



while True:
    print('''
╔═════ Options ═════╗
║                   ║
║ 0 - EXIT          ║
║ 1 - TEXT to HEX   ║
║ 2 - HEX to TEXT   ║
║                   ║
╚═══════════════════╝
    ''')
    try:
        opt = int(input('Select option: '))
    except ValueError:
        print('Invalid Choice. Try again.')
        continue
    if opt != 0 and opt != 1 and opt != 2:
        print('Invalid Choice. Try again.')
    elif opt == 0:
        break
    elif opt == 1:
        encoding()
    elif opt == 2:
        decoding()
    print('\nTry Again (Y/N)?: ', end='')
    try:
        try_again = str(input('')).lower()
    except ValueError:
        print('Invalid Choice. Try again.')
        continue
    if try_again == 'n':
        break