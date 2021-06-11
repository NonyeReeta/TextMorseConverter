chars = "abcdefghijklmnopqrstuvwsyz1234567890,.@/?'=()! "
morse_codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
               ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----", "..---",
               "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----", "--..--", ".-.-.-", ".--.-.",
               "-..-.", "..--..", ".----.", "-...-", "-.--.", "-.--.-", "-.-.--", "/"]
text_morse = {}
n = 0
for char in chars:
    text_morse[char] = morse_codes[n]
    n += 1
print("Welcome to the Text to Morse Code converter")
translate = True
while translate:
    user_input = input("Enter a word, phrase or sentence you would like to convert to morse code: ").lower()
    code = ""
    for word in user_input:
        for letter in word:
            if letter in text_morse:
                code += f"{text_morse[letter]} "
    print(f"Note the each letter is separated by a space and each word by '/': \nThis is your Morse code: {code}")
    translate_again = input("Do you want to translate again? Type 'yes' or 'no': ").lower()
    if translate_again == "yes":
        translate = True
    else:
        print("Thank you for using my command line Text-Morse Converter")
        translate = False
