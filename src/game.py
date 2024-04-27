import numpy as np

def pick_fallacy():
    fallacies = ["straw-man", "slippery slope", "fallacy fallacy", "false-dilemma", "sunk cost", "ad hominen"]
    fallacy_index = np.random.randint(0, len(fallacies) - 1)
    current_fallacy = fallacies[fallacy_index]
    return current_fallacy
    
def pick_conspiracy_theory():
    conspiracies = ["the moon is made of cheese", "the earth is flat", "the moon landing was fake", "birds aren't real", "the sun is a giant lamp", "all trees are made of plastic", "the birds work for the bourgeosie", "windows were invented by a person who hates birds", "bees aren't real and are actually robots", "the healthiest food ever is ice cream"]
    conspiracy_index = np.random.randint(0, len(conspiracies) - 1)
    current_conspiracy = conspiracies[conspiracy_index]
    return current_conspiracy

def generate_options(correct_fallacy):
    #generate options
    a = pick_fallacy()
    b = pick_fallacy()
    while(b == a or b == correct_fallacy):
        b = pick_fallacy()
    c = pick_fallacy()
    while(c == b or c == a or c == correct_fallacy):
        c = pick_fallacy()
    d = pick_fallacy()
    while(d == c or d == b or d == a or d == correct_fallacy):
        d = pick_fallacy()
    options = [a, b, c, d]
    options[np.random.randint(0,3)] = correct_fallacy
    return options