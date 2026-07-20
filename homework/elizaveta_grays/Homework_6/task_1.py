text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
        'dignissim vitae libero')
text_to_list = text.split()
new_list = []
for word in text_to_list:
    if word.endswith(',') or word.endswith('.'):
        punct = word[-1]
        clean_word = word[:-1]
        new_word = clean_word + 'ing'
        new_word_with_punct = new_word + punct
        new_list.append(new_word_with_punct)
    else:
        new_word = word + 'ing'
        new_list.append(new_word)
new_text = ' '.join(new_list)
print(new_text)
