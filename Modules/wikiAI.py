import wikipedia
from speechRecAI import SpeechAI
from subprocess import call
from mirror import respond

def word_meaning(word):
    ny = wikipedia.page(word)
    respond("Here's some information on " + word, {
    	"type": "wikipedia",
    	"word": word,
    	"summary": ny.summary
	})

if __name__=="__main__":
    word_meaning("dictionary")
