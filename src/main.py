import llm
import game

def main():
    print("An AI-generated prompt will be shown to you.\nYou have to decide which logical fallacy it uses.")
    loop = True
    while loop:
        fallacy = game.pick_fallacy()
        conspiracy_theory = game.pick_conspiracy_theory()

        input = "Use the " + fallacy + " to prove that " + conspiracy_theory + "."
        prompt = llm.generate_prompt(input)

        options = game.generate_options(fallacy)

        print("Prompt: " + prompt)
        print("Answers: ")
        for i in range(4):
            print(str(i+1) + ". " + options[i])
        
        answer = input("Enter the number of the correct answer: ")
        if fallacy == options[int(answer)-1]:
            print("Correct!")
        else:
            print("Incorrect. The correct answer was: " + fallacy)