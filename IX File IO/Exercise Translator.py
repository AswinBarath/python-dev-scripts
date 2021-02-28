from translate import Translator
try:
    with open('./test.txt', mode='r') as file:
        text = file.read()
        print(text)
        translator = Translator(to_lang="ja")
        translated_text = translator.translate(text)
        print(translated_text)
        translator = Translator(to_lang="hi")
        hindi = translator.translate(text)
        print(hindi)
        translator = Translator(to_lang="ta")
        tamil = translator.translate(text)
        print(tamil)
        translator = Translator(to_lang="ar")
        arabic = translator.translate(text)
        print(arabic)
        with open('./test-translated.txt', mode='w') as file2:
            # file2.write('Japanese\n')
            file2.write(translated_text)
            # file2.write('Hindi\n')
            # file2.write(hindi)
            # file2.write('Tamil\n')
            # file2.write(tamil)
            # file2.write('Arabic\n')
            # file2.write(arabic)
            # unicodeData = 'Japanese\n' + translated_text + '\nHindi\n' + hindi + '\nTamil\n' + tamil + '\nArabic\n' + arabic
            # print(unicodeData.encode('utf-8', 'ignore'))
            # file2.write(unicodeData)
except FileNotFoundError as e:
    print('File is missing', e)
