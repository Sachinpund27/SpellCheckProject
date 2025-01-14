from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self,text):
        words = text.split()
        corrected_wors = []

        for word in words:
            corrected_words = self.spell.correction(word)
            if corrected_words != word.lower():
                print(f'Correcting "{word}" to "{corrected_words}"')
                corrected_wors.append(corrected_words)


        return ' '.join(corrected_wors)
    
    def run (self):
        print("\n---Spell Checker---")

        while True:
            text = input ('Enter text to check (or type "Exit" to quit): ')

            if text.lower() == 'exit':
                print('Closing the program......')
                break

            corrected_text = self.correct_text(text)
            print(f'Corrected Text : {corrected_text}')

if __name__ == "__main__":
    SpellCheckerApp().run()