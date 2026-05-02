import demoji # demoji is a module installed using pip. It is used to import emoji codes from unicode

def replaceEmoji(text): # the first method replaces all emojis as blank text
    newText = demoji.replace(text, '') # this replaces all demoji characters as blank
    return(newText)

def textReplace(text): # the second method replaces all emojis with built-in descriptions in demoji
    newText = demoji.replace_with_desc(text)
    return(newText)

def findEmoji(text): # finds all emojis in a given string and gives descriptions
    emojis = demoji.findall(text) # the findall method returns a list of pairs seperated by a : the first is the emoji, the second is its description
    return(emojis)

if __name__ == '__main__':
    test = 'hello! ☀️🌸'

    print(replaceEmoji(test))
    print(textReplace(test))
    print(findEmoji(test))