def getWordScore(word):
    scoreSoFar = 0
    for i in word:
        scoreSoFar +=SCRABBLE_LETTER_VALUES[i]
    scoreSoFar*=len(word)
    return scoreSoFar
        
