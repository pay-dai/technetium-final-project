# Daija Porter
# Function to randomly select a language and 
# generate hints from the selected language

import random

# Example language dictionary with the language as keys and the hints as values.
languages = {
    "Korean": {
        "firstlang": "80 million",
        "region": "East Asia",
        "history": "In the 1400s, a king introduced an alphabet whose letters "
                 "included shapes based on the position of the tongue and lips.",
    },
    "Icelandic": {
        "firstlang": "350,000",
        "region": "an island in the North Atlantic",
        "history": "Medieval writers used this language to tell sagas about "
                   "family feuds, sea voyages, and Viking settlers.",
    },
}

def randomlang_hints(languages, used_languages):
    unused = []
    for lang in languages:
        if lang not in used_languages:
            unused.append(lang)

    if not unused:
        raise ValueError("No unused languages remain.")

    correct_language = random.choice(unused)
    facts = languages[correct_language]

    hints = [
        f"Around {facts['firstlang']} people speak it as their first language.",
        f"This language is spoken in {facts['region']}.",
        facts["history"],
    ]

    return {"correct_language": correct_language, "hints": hints}

if __name__ == "__main__":
    round_data = randomlang_hints(languages, ["Korean"])
    print(round_data["correct_language"])
    for hint in round_data["hints"]:
        print(hint)
        