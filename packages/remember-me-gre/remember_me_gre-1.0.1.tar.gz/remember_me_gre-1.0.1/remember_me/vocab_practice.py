import random
from colorama import Fore, Style, init
from remember_me.vocab_loader import load_vocabulary
from remember_me.starlist_manager import StarListManager
# from vocab_loader import load_vocabulary
# from starlist_manager import StarListManager
from openai import OpenAI
import os

MOONSHOT_API_KEY = os.getenv("MOONSHOT_API_KEY")

if MOONSHOT_API_KEY is None:
    raise ValueError("Please set the MOONSHOT_API_KEY environment variable.")


client = OpenAI(
    api_key=MOONSHOT_API_KEY, # 在这里将 MOONSHOT_API_KEY 替换为你从 Kimi 开放平台申请的 API Key
    base_url="https://api.moonshot.cn/v1",
)
 

class TextColors:
    HEADER = '\033[95m'       # Light Magenta
    OKBLUE = '\033[94m'       # Light Blue
    OKCYAN = '\033[96m'       # Light Cyan
    OKGREEN = '\033[92m'      # Light Green
    WARNING = '\033[93m'      # Light Yellow
    PINK = '\033[95m'         # Pink
    LIGHT_BLUE = '\033[94m'   # Light Blue
    FAIL = '\033[91m'         # Light Red
    LIGHT_RED = '\033[91m'    # Shallow Red
    LIGHT_MAGENTA = '\033[95m'# Shallow Magenta
    LIGHT_YELLOW = '\033[93m' # Shallow Yellow
    LIGHT_WHITE = '\033[97m'  # White (Bright)
    LIGHT_GRAY = '\033[90m'   # Light Gray
    BOLD = '\033[1m'          # Bold
    UNDERLINE = '\033[4m'     # Underline
    ENDC = '\033[0m'          # Reset color

def validate_meaning_with_fallback(word, input_meaning, correct_meaning):
    """
    First validate using streak method. If it fails, fallback to AI validation.
    """
    is_valid_streak = validate_meaning(input_meaning, correct_meaning)
    if is_valid_streak:
        return True

    # If streak method fails, fallback to AI validation
    print("Local validation failed. Querying AI for validation...")
    is_valid_ai = validate_with_ai(word, input_meaning)
    return is_valid_ai


def validate_with_ai(word, input_meaning):
    try:
        # Send a request to the Moonshot API
        response = client.chat.completions.create(
            model="moonshot-v1-8k",
            messages=[
                {
                    "role": "user",
                    "content": (
                        f"Hello! I'm trying to validate the meaning of a word. "
                        f"Confirm if the user's input meaning '{input_meaning}' is a valid synonym or meaning of word {word} in question."
                        "Only return yes, or no."
                    ),
                },
            ],
            temperature=0.3,
        )

        # Ensure the response contains the expected structure
        if response.choices and len(response.choices) > 0:
            ai_reply = response.choices[0].message.content.strip().lower()
            print(f"AI reply: {ai_reply}")  # Log the AI response for debugging
            return ai_reply.count("yes") > 0 or ai_reply.count("Yes") > 0
        else:
            print("Unexpected response structure from the AI API.")
            print(response)
            return False

    except Exception as e:
        # Enhanced error logging
        print(f"AI validation failed: {e}")
        return False



def preprocess_meaning(meaning):
    # Split meaning into individual characters for Chinese
    return set(meaning)

def calculate_max_streak(input_text, correct_text):
    input_chars = list(input_text)
    correct_chars = list(correct_text)

    max_streak = 0
    current_streak = 0

    i, j = 0, 0
    while i < len(input_chars) and j < len(correct_chars):
        if input_chars[i] == correct_chars[j]:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
            i += 1
            j += 1
        else:
            current_streak = 0
            if j < len(correct_chars) - 1:
                j += 1
            else:
                i += 1
                j = 0

    return max_streak

def validate_meaning(input_meaning, correct_meaning):
    # Preprocess both input and correct meanings
    input_chars = set(input_meaning)
    correct_chars = preprocess_meaning(correct_meaning)

    # Check overlap of characters
    overlap = input_chars & correct_chars
    # print(f"input_chars: {input_chars}")
    # print(f"correct_chars: {correct_chars}")
    # print(f"The overlap is: {overlap}")

    # Calculate maximum streak of matching characters
    max_streak = calculate_max_streak(input_meaning, correct_meaning)
    streak_threshold = len(correct_meaning) * 0.5  # Adjust threshold as needed (50% here)

    # print(f"Maximum Streak: {max_streak}, Required Threshold: {streak_threshold}")

    # Check if the overlap or streak is sufficient
    return len(overlap) > 2 or max_streak >= streak_threshold

def learning_mode(vocabulary, starlist_manager):
    """
    Learning mode for all words in the vocabulary.
    """
    print("\nEntering Learning Mode...")
    general_learning_mode(vocabulary, starlist_manager=starlist_manager)

def testing_mode(vocabulary, starlist_manager=None):
    """
    Testing mode for all words in the vocabulary.
    """
    print("\nEntering Testing Mode...")
    general_testing_mode(vocabulary, starlist_manager=starlist_manager)

###################################SECTION TESTING MODE IMPLEMENTATION###################################
def section_testing_mode(sections, current_section=None, starlist_manager=None):
    """
    Testing mode for words in a specific section, with navigation options to
    move to the next section, previous section, or retest the current section.
    """
    if not current_section:
        print("Available Sections:")
        section_names = sorted(
            [name for name in sections.keys() if name.startswith("Section")],
            key=lambda x: int(x.split(" ")[1])
        ) + [name for name in sections.keys() if not name.startswith("Section")]
        
        for section_name in section_names:
            print(f"- {section_name}")

        current_section = input("\nEnter the section name to test (e.g., Section 1): ").strip()
        if current_section not in sections:
            print("Invalid section name. Returning to main menu.")
            return

    while True:
        section_words = sections[current_section]
        print(f"\nEntering Section Testing Mode for {current_section}...")
        general_testing_mode(section_words, section_name=current_section, starlist_manager=starlist_manager)

        print("\nSection Completed!")
        print("Navigation Options:")
        print("r: Retest this section")
        print("p: Go to the previous section")
        print("n: Go to the next section")
        print("q: Return to main menu")

        navigation_input = input("Enter your choice (r/p/n/q): ").strip().lower()

        section_names = sorted(
            [name for name in sections.keys() if name.startswith("Section")],
            key=lambda x: int(x.split(" ")[1])
        ) + [name for name in sections.keys() if not name.startswith("Section")]
        
        current_index = section_names.index(current_section)

        if navigation_input == 'r':
            print(f"\nRetesting {current_section}...")
        elif navigation_input == 'p':
            if current_index > 0:
                current_section = section_names[current_index - 1]
                print(f"\nSwitching to {current_section}...")
            else:
                print("This is the first section. Cannot go back further.")
        elif navigation_input == 'n':
            if current_index < len(section_names) - 1:
                current_section = section_names[current_index + 1]
                print(f"\nSwitching to {current_section}...")
            else:
                print("This is the last section. Cannot go further.")
        elif navigation_input == 'q':
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")

def general_testing_mode(words_to_test, section_name=None, starlist_manager=None):
    """
    Handles both general testing and section testing modes.
    """
    total_words = len(words_to_test)
    correct_count = 0
    incorrect_count = 0
    tested_words = 0

    if total_words == 0:
        print("No words available for testing.")
        return

    if section_name:
        print(f"\nTesting words in section: {section_name}")
    else:
        print("\nTesting all words.")

    # Shuffle words to ensure random order
    random.shuffle(words_to_test)

    while tested_words < total_words:
        word = words_to_test[tested_words]
        print(f"\n{TextColors.OKCYAN}{TextColors.BOLD}Word:{TextColors.ENDC} {TextColors.BOLD}{TextColors.OKGREEN}{word['word']}{TextColors.ENDC} ({tested_words + 1}/{total_words})")
        print(f"{TextColors.WARNING}{TextColors.BOLD}Incorrect so far:{TextColors.ENDC} {incorrect_count}")

        user_input = input("Command ('h' for help): ").strip().lower()
        if user_input == 'q':
            print("Are you sure you want to quit the test? (y/n)")
            confirm = input().strip().lower()
            if confirm == 'y':
                print("Exiting test...")
                return
            else:
                print("Resuming test...")
        elif user_input == 'h':
            print("\nPress 's' to star this word, \n'q' to quit, \nor press Enter to pass(counted as incorrect).")
        elif user_input == 's':
            print(starlist_manager.add_to_star_list(word))
        elif user_input == '':
            print(f"Passed. You did not provide the meaning of the word! \nThe correct meaning is: {TextColors.BOLD}{TextColors.LIGHT_YELLOW}{word['definition']}{TextColors.ENDC}")
            incorrect_count += 1
        elif validate_meaning_with_fallback(word['word'], user_input, word['definition']):
            print(f"{TextColors.OKGREEN}{TextColors.BOLD}Correct! Great job!{TextColors.ENDC}")
            print(f"The definition is: {TextColors.BOLD}{TextColors.LIGHT_YELLOW}{word['definition']}{TextColors.ENDC}")
            correct_count += 1
        else:
            print(f"Incorrect. The correct meaning is: {TextColors.BOLD}{TextColors.LIGHT_YELLOW}{word['definition']}{TextColors.ENDC}")
            incorrect_count += 1

        tested_words += 1

    correctness_rate = (correct_count / total_words) * 100 if total_words > 0 else 0
    print(f"\nTest completed! Correctness rate: {correct_count}/{total_words} = {correctness_rate:.2f}%")
###################################END OF SECTION TESTING MODE IMPLEMENTATION###################################

def general_learning_mode(words_to_learn, section_name=None, starlist_manager=None):
    """
    Handles both general learning and section learning modes.
    """
    total_words = len(words_to_learn)
    if total_words == 0:
        print("No words available for learning.")
        return

    if section_name:
        print(f"\nLearning words in section: {section_name}")
    else:
        print("\nLearning all words.")

    print("Select Learning Method:")
    print("1. In Order of the Original List")
    print("2. Random but Exhaustive")
    learning_method = input("Enter 1 or 2 to select method: ").strip()

    if learning_method == '1':
        print("\nEntering Learning Mode in Order...")
    elif learning_method == '2':
        print("\nEntering Random Learning Mode...")
        random.shuffle(words_to_learn)
    else:
        print("Invalid selection. Returning to main menu.")
        return

    index = 0
    learned_words = 0

    while index < len(words_to_learn):
        word = words_to_learn[index]
        print(f"\n{TextColors.OKGREEN}Word:{TextColors.ENDC} {TextColors.BOLD}{TextColors.OKBLUE}{word['word']}{TextColors.ENDC} ({index + 1}/{total_words})")
        show_meaning = False

        while True:
            command = input("Command ('h' for help): ").strip().lower()
            if command == 'h':
                print("\nPress 'm' to show the meaning, \n'p' to go to the previous word, \n's' to star this word, \n'ex' for example sentence, \n'q' to quit, \n or press Enter to continue.")
            elif command == 'm':
                if not show_meaning:
                    print(f"{TextColors.LIGHT_GRAY}Def: {TextColors.BOLD}{TextColors.LIGHT_RED}{word['definition']}{TextColors.ENDC}")
                    show_meaning = True
            elif command == 's':
                print(starlist_manager.add_to_star_list(word))
            elif command == 'r':
                print(starlist_manager.remove_from_star_list(word))
            elif command == 'p':
                if index > 0:
                    index -= 1
                    break  # Move to the previous word
                else:
                    print("This is the first word. Cannot go back further.")
            elif command == 'ex':
                print("Generating an example sentence and its Chinese translation...")
                response = client.chat.completions.create(
                    model="moonshot-v1-8k",
                    messages=[
                        {
                            "role": "user",
                            "content": (
                                f"Provide a short example sentence using the word '{word['word']}' in the context of its meaning -'{word['definition']}'"
                                "The sentence should be concise and illustrative. Also, provide a Chinese translation of the example sentence. You MUST separate the example sentence and translation with a newline."
                            ),
                        },
                    ],
                    temperature=0.3,
                )

                # Display the example sentence and its translation
                if response.choices and len(response.choices) > 0:
                    ai_reply = response.choices[0].message.content.strip()
                    parts = ai_reply.split("\n")
                    example_sentence = parts[0].strip() if len(parts) > 0 else "N/A"
                    translation = parts[1].strip() if len(parts) > 1 else "N/A"

                    print(f"Example Sentence: {TextColors.LIGHT_MAGENTA}{example_sentence}{TextColors.ENDC}")
                    print(f"Translation     : {TextColors.LIGHT_YELLOW}{translation}{TextColors.ENDC}")
                    print(f"For Debugging: {ai_reply}")
                else:
                    print("Failed to generate an example sentence and translation.")
            elif command == 'q':
                print("Returning to main menu...")
                return
            elif command == '':
                index += 1
                learned_words += 1
                break  # Move to the next word
            else:
                print("Invalid command. Enter 'h' for help.")

    print(f"\nCongratulations! You have completed learning all words. Progress: {total_words}/{total_words}.")
    

###################################SECTION LEARNING MODE IMPLEMENTATION###################################
def section_learning_mode(sections, current_section=None, starlist_manager=None):
    """
    Learning mode for words in a specific section, with navigation options to
    move to the next section, previous section, or retest the current section.
    """
    if not current_section:
        print("Available Sections:")
        section_names = sorted(
            [name for name in sections.keys() if name.startswith("Section")],
            key=lambda x: int(x.split(" ")[1])
        ) + [name for name in sections.keys() if not name.startswith("Section")]
        
        for section_name in section_names:
            print(f"- {section_name}")

        current_section = input("\nEnter the section name to learn (e.g., Section 1): ").strip()
        if current_section not in sections:
            print("Invalid section name. Returning to main menu.")
            return

    while True:
        section_words = sections[current_section]
        print(f"\nEntering Section Learning Mode for {current_section}...")
        general_learning_mode(section_words, section_name=current_section, starlist_manager=starlist_manager)

        print("\nSection Completed!")
        print("Navigation Options:")
        print("r: Retest this section")
        print("p: Go to the previous section")
        print("n: Go to the next section")
        print("q: Return to main menu")

        navigation_input = input("Enter your choice (r/p/n/q): ").strip().lower()

        section_names = sorted(
            [name for name in sections.keys() if name.startswith("Section")],
            key=lambda x: int(x.split(" ")[1])
        ) + [name for name in sections.keys() if not name.startswith("Section")]
        
        current_index = section_names.index(current_section)

        if navigation_input == 'r':
            print(f"\nRetesting {current_section}...")
        elif navigation_input == 'p':
            if current_index > 0:
                current_section = section_names[current_index - 1]
                print(f"\nSwitching to {current_section}...")
            else:
                print("This is the first section. Cannot go back further.")
        elif navigation_input == 'n':
            if current_index < len(section_names) - 1:
                current_section = section_names[current_index + 1]
                print(f"\nSwitching to {current_section}...")
            else:
                print("This is the last section. Cannot go further.")
        elif navigation_input == 'q':
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")
###################################END OF SECTION LEARNING MODE IMPLEMENTATION###################################

def starlist_manager_session(starlist_manager):
    while True:
        print("\nStar List Management:")
        print("1. Clear the star list")
        print("2. Remove word from star list by index")
        print("3. Display star list")
        print("4. Test star list")
        print("5. Learn star list")
        print("6. Add word pair manually to star list")
        print("7. Exit star list management")

        command = input("Enter the number to select an option: ").strip()
        if command == '1':
            decision = input("Are you sure you want to clear the star list? (y/n): ").strip().lower()
            if decision == 'y':
                starlist_manager.starred_words.clear()
                print("Star list has been cleared.")
            else:
                print("Clear operation cancelled.")
            
        elif command == '2':
            # Display the current star list with indices
            print("\nStarred Words:")
            for idx, word in enumerate(starlist_manager.starred_words):
                print(f"{idx}: {word['word']} - {word['definition']}")

            try:
                index = int(input("Enter the index of the word to remove: ").strip())
                if 0 <= index < len(starlist_manager.starred_words):
                    removed_word = starlist_manager.starred_words.pop(index)
                    print(f"Removed: {removed_word['word']} - {removed_word['definition']}")
                else:
                    print("Invalid index. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif command == '3':
            print(starlist_manager.display_star_list())
        elif command == '4':
            print("\nEntering Testing Mode for Starred Words...")
            testing_mode(starlist_manager.starred_words)
        elif command == '5':
            print("\nEntering Learning Mode for Starred Words... Shuffling...")
            shuffled_words = starlist_manager.starred_words[:]
            random.shuffle(shuffled_words)
            learning_mode(shuffled_words, starlist_manager=starlist_manager)
        elif command == '6':
            word = input("Enter the word: ").strip()
            definition = input("Enter the definition: ").strip()
            print(starlist_manager.add_to_star_list({'word': word, 'definition': definition}))
        elif command == '7':
            print("Exiting star list management...")
            break
        else:
            print("Invalid command. Please try again.")

def random_vocabulary_practice(vocabulary, sections, starlist_manager):
    if not vocabulary:
        print("No vocabulary found!")
        return

    while True:
        print("\nSelect Mode:")
        print(f"1. Learning Mode (Learn {len(vocabulary)} words!!)")
        print(f"2. Testing Mode (Test {len(vocabulary)} words!!)")
        print("3. Section Testing Mode (Test by specific section)")
        print("4. Section Learning Mode (Learn by specific section)")
        print("5. Manage starred words")
        print("q. Quit Program")

        mode = input("Enter your choice: ").strip().lower()
        if mode == '1':
            print("\nEntering Learning Mode...")
            learning_mode(vocabulary, starlist_manager=starlist_manager)
        elif mode == '2':
            print("\nEntering Testing Mode...")
            testing_mode(vocabulary, starlist_manager=starlist_manager)
        elif mode == '3':
            print("\nEntering Section Testing Mode...")
            section_testing_mode(sections, starlist_manager=starlist_manager)
        elif mode == '4':
            print("\nEntering Section Learning Mode...")
            section_learning_mode(sections, starlist_manager=starlist_manager)
        elif mode == '5':
            starlist_manager_session(starlist_manager)
        elif mode == 'q':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

def main():
    print("-------------------------------------------------------------------------------------------------")
    print(r"""
 ███████████                                                     █████                           ██████   ██████         
░░███░░░░░███                                                   ░░███                           ░░██████ ██████          
 ░███    ░███   ██████  █████████████    ██████  █████████████   ░███████   ██████  ████████     ░███░█████░███   ██████ 
 ░██████████   ███░░███░░███░░███░░███  ███░░███░░███░░███░░███  ░███░░███ ███░░███░░███░░███    ░███░░███ ░███  ███░░███
 ░███░░░░░███ ░███████  ░███ ░███ ░███ ░███████  ░███ ░███ ░███  ░███ ░███░███████  ░███ ░░░     ░███ ░░░  ░███ ░███████ 
 ░███    ░███ ░███░░░   ░███ ░███ ░███ ░███░░░   ░███ ░███ ░███  ░███ ░███░███░░░   ░███         ░███      ░███ ░███░░░  
 █████   █████░░██████  █████░███ █████░░██████  █████░███ █████ ████████ ░░██████  █████        █████     █████░░██████ 
░░░░░   ░░░░░  ░░░░░░  ░░░░░ ░░░ ░░░░░  ░░░░░░  ░░░░░ ░░░ ░░░░░ ░░░░░░░░   ░░░░░░  ░░░░░        ░░░░░     ░░░░░  ░░░░░░  
                                                                                                                                                                                                                                           
                                                                                                                                                        
    """)
    print("Welcome to Vocabulary Practice!")
    print("\nThis is an AI-powered tool to help you memorize GRE words in the fastest way possible!")

    config_file = "config.txt"

    def read_config():
        if os.path.exists(config_file):
            with open(config_file, 'r') as file:
                lines = file.readlines()
                if len(lines) >= 2:
                    return lines[0].strip(), lines[1].strip()
        return None, None

    def write_config(vocab_path, starlist_path):
        with open(config_file, 'w') as file:
            file.write(f"{vocab_path}\n")
            file.write(f"{starlist_path}\n")

    vocab_path, starlist_path = read_config()

    if vocab_path and starlist_path:
        print(f"Reading vocabulary file from: {vocab_path}")
        print(f"Reading star list file from: {starlist_path}")
        change = input("Do you want to change these files? (y/n): ").strip().lower()
        if change == 'y':
            vocab_path = None
            starlist_path = None

    while not vocab_path:
        vocab_path = input("Enter the path to the vocabulary file (e.g. word_sheets/Word_Sheet1.csv): ").strip()
        if not os.path.exists(vocab_path):
            print("Vocabulary file not found. Would you like to try again? (y/n)")
            retry = input().strip().lower()
            if retry != 'y':
                print("Exiting program. Goodbye!")
                exit()
            vocab_path = None

    while not starlist_path:
        starlist_path = input("Enter the path to the star list file (e.g. star_words/starred.csv): ").strip()
        try:
            starlist_manager = StarListManager(starlist_path)
        except FileNotFoundError:
            print("Star list file not found. Would you like to try again? (y/n)")
            retry = input().strip().lower()
            if retry != 'y':
                print("Exiting program. Goodbye!")
                exit()
            starlist_path = None

    write_config(vocab_path, starlist_path)
    vocabulary, sections = load_vocabulary(vocab_path)
    starlist_manager = StarListManager(starlist_path)
    try:
        random_vocabulary_practice(vocabulary, sections, starlist_manager)
    finally:
        starlist_manager.save_starred_words()
    
    
if __name__ == "__main__":
    main()