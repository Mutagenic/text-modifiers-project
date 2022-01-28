def pascalize(text):
    """Pascalizes a given text removing _ and space"""
    text = text.strip()

    edited_text = text.replace("_", " ")
    words_list = edited_text.split(" ")
    new_text = []
    for word in words_list:
        if not word:
            continue

        titlecase = word[0].upper()
        new_text.append(titlecase + word[1:])

    return "".join(new_text)


def depascalize(text):
    """Depascalizes given text into a text seperated by _
    where there would be spaces"""
    text = text.strip()
    text = text[0].upper() + text[1:]

    chunk = None
    chunks_list = []
    for char in text:
        if str(char).isupper():
            if chunk:
                chunks_list.append(chunk)

            chunk = str(char).lower()
        else:
            chunk += str(char)

    if chunk:
        chunks_list.append(chunk)
    return "_".join(chunks_list)


def camelize(text):
    """Makes the first character of text lower case,
    removes spaces and makes every character after a space upper case,
    or if there are no spaces in text, add _ before every upper case character
    """
    text = text.strip()
    edited_text = text.replace(".", "")

    if " " not in edited_text:
        return depascalize(edited_text)

    split_text = edited_text.split(" ")

    edited_words_list = [split_text[0].lower()]

    split_text.pop(0)
    pascalized_part = pascalize(" ".join(split_text))
    edited_words_list.append(pascalized_part)
    return "".join(edited_words_list)


def is_pascalize(text):
    """Check if a text is pascalized"""
    text = text.strip()
    return str(text[0]).isupper()


def is_camelcase(text):
    """Check if a text is camelcase"""
    text = text.strip()
    if not str(text[0]).islower():
        return False
    else:
        for char in text:
            if str(char).isupper():
                return True

    return False


def is_snakecase(text):
    """Check if a text is snakecase"""
    text = text.strip()
    if not text.islower():
        return False
    else:
        return True
