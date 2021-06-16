from translate import Translator

translator = Translator(to_lang="de")
try:
    with open('./simplefile.txt', mode='r') as my_file:
        text = my_file.read()
        print(text)
        translation = translator.translate(text)
        print(translation)
        with open('./simplefile-ja.txt', mode='w') as my_file1:
            assert isinstance(translation, object)
            my_file1.write(str(translation))
except FileNotFoundError as err:
    print('Check your file path')
