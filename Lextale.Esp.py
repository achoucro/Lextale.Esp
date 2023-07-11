from psychopy import visual, core, event
import random

# Provided lists of real words and non-words
words = [word.upper() for word in ["pellizcar", "pulmones", "zapato", "tergiversar", "pésimo",
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

# Mix them together and randomize the order
stimuli = words + nonwords
random.shuffle(stimuli)

# Create a window
win = visual.Window([800, 600])

colorSpace = [1,1,1]

# Create a clock to measure response time
clock = core.Clock()

# Create a fixation cross
fixation = visual.TextStim(win, text="+", pos=(0, 0))

# Create instruction text
instructions = visual.TextStim(win, 
                               text="You will be shown 90 words, one at a time. "
                                    "Your task is to decide whether this is a real Spanish word, or completely made up. "
                                    "If you think it is a real Spanish  word, click the 'y' key, for YES."
                                    "If you think it is a made up word that only looks spanish, click the 'n' key, for NO."
                                    "When you're ready to begin, press the SPACE bar.",
                               wrapWidth=1.5)

# Show instructions
instructions.draw()
win.flip()

# Wait for a space bar press to continue
event.waitKeys(keyList=["space"])

# Start the lexical decision task
for word in stimuli:
    # Show the fixation cross
    fixation.draw()
    win.flip()

    # Wait for a moment before presenting the stimulus
    core.wait(1.0)  # this wait time can be adjusted

    # Show the word
    text = visual.TextStim(win, text=word)
    text.draw()
    win.flip()

    # Start the timer
    clock.reset()

    # Wait for a response
    keys = event.waitKeys(keyList=["y", "n"])

    # Calculate response time
    response_time = clock.getTime()

    # Record the response and the response time
    print(word, keys[0], response_time)

    # Introduce a delay between trials
    core.wait(1.0)

win.close()

