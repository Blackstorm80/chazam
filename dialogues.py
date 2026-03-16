dataset = {
    "greetings": [
        "Bonjour!",
        "Salut, comment ça va ?",
        "Hello, ravi de vous voir !",
        "Coucou !",
        "Bienvenue sur Chazam."
    ],
    "farewells": [
        "Au revoir !",
        "À la prochaine !",
        "Bonne journée.",
        "Bye bye !",
        "À bientôt."
    ],
    "bot_info": [
        "Je suis le bot Chazam, votre assistant musical.",
        "Mon intelligence est en cours d'entraînement.",
        "Je peux vous aider à identifier des chansons."
    ],
    "errors": [
        "Désolé, je n'ai pas compris.",
        "Pouvez-vous répéter ?",
        "Oups, quelque chose s'est mal passé."
    ]
}

def get_dialogues(category):
    return dataset.get(category, [])