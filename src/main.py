
import llm
import game

def main():
    while True:
        play = input("Would you like to play? (y/n)")
        if (play == "n"):
            break
        play_game()
    
def play_game():
    print("An AI-generated prompt will be shown to you.\nYou have to decide which logical fallacy it uses.")
    loop = True
    score = 0
    while loop:
        fallacy = game.pick_fallacy()
        conspiracy_theory = game.pick_conspiracy_theory()

        llm_input = "Use the " + fallacy + " to prove that " + conspiracy_theory + "."
        prompt = llm.generate_prompt(llm_input)

        options = game.generate_options(fallacy)

        print("Prompt: " + prompt)
        print("Answers: ")
        for i in range(4):
            print(str(i+1) + ". " + options[i])
        
        answer = input("Enter the number of the correct answer: ")
        if fallacy == options[int(answer)-1]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer was: " + fallacy)
            print("Your score is: " + score)
            print("Game Over.")
            loop = False



main()
play_game

