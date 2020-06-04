from translate import Translator

try:
    with open('translate.txt', mode='r') as my_file:
        original = my_file.read()
        print(f'Original: {original}')
        language = Translator(to_lang='es', from_lang='en')
        translation = language.translate(original)
        print(f'\nTranslation: {translation}')
        with open('translated-es.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as err:
    print('File does not exist in this directory')

# Output:
# Original: Hi this is Manuel, please translate this shit nigga

# Translation: Hola, soy Manuel, por favor traduce esta mierda nigga
