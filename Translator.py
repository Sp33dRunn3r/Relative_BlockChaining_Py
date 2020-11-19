from translate import Translator


def convert_to_spanish(data):
    translator = Translator(to_lang="es")
    user_input = input('''
    ¿Traducir estadísticas al español? 
    
    (Escribe \"Sí\" o \"No\") 
    (To conitnue in English, type "Continue")
    
    ''')
    for response in user_input:
        if user_input.startswith("s"):
            print("Traduciendo al español ...")
            translation = translator.translate(data)
            print(translation)
            break
        elif user_input.startswith("n") or user_input.startswith("c"):
            print("Continuing in English")
            print(data)
            break
        elif user_input != user_input.startswith("s") or user_input != user_input.startswith("n") or user_input != user_input.startswith("c"):
            print("Respuesta invalida, Invalid response...")
            break

