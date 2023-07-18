from psychopy import visual, core, event
import random
import pandas as pd 
import uuid
from collections import Counter

realwords = [word.upper() for word in ["pellizcar", "pulmones", "zapato", "tergiversar", "pésimo",
         "hacha", "canefa", "asesinato", "helar", "yunque", "Regar",
         "ávido", "lacayo", "látigo", "bisagra", "secuestro", "merodear",
         "pandilla", "aviso", "loro", "granuja", "estornudar", "torpe",
         "alfombra", "rebuscar", "canela", "cuchara", "jilguero",
         "martillo", "ladrón", "ganar", "candado", "camisa", "fomentar",
         "nevar", "musgo", "tacaño", "besar", "matar", "seda", "flaco",
         "orgulloso", "bizcocho", "cabello", "alegre", "engatusar",
         "polvoriento", "hervidor", "yacer", "atar", "tiburón",
         "frondoso", "hormiga", "pozo", "guante", "laud", "barato",
         "acantilado", "prisa", "clavel"]]

nonwords = [word.upper() for word in ["terzo", "batillón", "cadeña", "antar", "abracer",
            "floroso", "arsa", "brecedad", "capillo", "lampera",
            "acutación", "decar", "alardio", "fatacidad", "pauca",
            "rompido", "cadallo", "cartinar", "flamida", "vegada",
            "plaudir", "esposante", "hacido", "temblo", "pemición",
            "cintro", "tropaje", "empirador", "escuto", "grodo"]]

correct_responses = {word: "y" for word in realwords}
correct_responses.update({word: "n" for word in nonwords})

participant_id = str(uuid.uuid4())

stimuli = realwords + nonwords
random.shuffle(stimuli)

win = visual.Window([800, 600], color='black')

clock = core.Clock()

fixation = visual.TextStim(win, text="+", pos=(0, 0))

instructions = visual.TextStim(win, 
                               text="You will be shown 90 words, one at a time. "
                                    "Your task is to decide whether this is a real Spanish word, or a completely made up word. "
                                    "If you think it is a real Spanish  word, click the 'y' key, for YES."
                                    "If you think it is a made up word that only looks spanish, click the 'n' key, for NO."
                                    "Please try to respond as quickly and as accurately as you can."
                                    "When you're ready to begin, press the SPACE bar.",
                               wrapWidth=1.5)

instructions.draw()
win.flip()
event.waitKeys(keyList=["space"])
results = []

for word in stimuli:
    fixation.draw()
    win.flip()
    core.wait(1.0) 
         
    text = visual.TextStim(win, text=word)
    text.draw()
    win.flip()
         
    clock.reset()
         
    keys = event.waitKeys(keyList=["y", "n"])
         
    response_time = clock.getTime()
         
    correct = int(keys[0] == correct_responses[word])
         
    word_type = "Real" if word in realwords else "Nonword"
    
    #counts = Counter(results)
    
    yes_to_realword = {response: realwords.count(response) for response in realwords if response == 'y'}
    no_to_nonword = {response: nonwords.count(response) for response in nonwords if response == 'n'}
    
    score = sum(yes_to_realword) / 60 + sum(no_to_nonword) / 30 
    Lextale_score = score / 2 
    
    results.append([word, word_type, keys[0], correct, response_time , Lextale_score])

df = pd.DataFrame(results, columns=["Word", "WordType", "Response", "Correct", "Response Time"]), 
(results, row=["Lextale_score"]) 
filename = f"results_{participant_id}.csv"
df.to_csv(filename, index=False)

win.close()


  
