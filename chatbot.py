import collections.abc
import collections

if not hasattr(collections, 'Hashable'):
    collections.Hashable = collections.abc.Hashable

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Initialisation
chazam_bot = ChatBot(
    "ChazamBot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.db",
    spacy_model_name="fr_core_news_sm",
    logic_adapters=[
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.MathematicalEvaluation"
    ]
)


# Fonction d'entrainement de base
def entrainer_base():
    trainer = ListTrainer(chazam_bot)
    conversations = [
        "Bonjour",
        "Bonjour ! Je suis Chazam, votre assistant botanique. Comment puis-je vous aider à trouver la plante parfaite ou à en prendre soin ?",
        "Qui t'a cree ?",
        "J'ai ete concu par l'equipe Blackstorm pour le module de gestion de projet, et j'ai été spécialisé dans le domaine de la botanique.",
        "Quel est l'objectif du projet ?",
        "Mon objectif est de vous assister dans vos recherches de plantes et de vous donner des conseils d'entretien. Ce projet valide aussi les competences Git et la collaboration en equipe."
    ]
    trainer.train(conversations)

# Fonction d'entrainement sur les plantes
def entrainer_sur_plantes():
    trainer = ListTrainer(chazam_bot)
    plantes_conversations = [
        "Quelles plantes recommandez-vous pour un débutant ?",
        "Pour un débutant, je recommande des plantes faciles d'entretien comme le Zamioculcas, le Sansevieria, ou le Pothos.",
        "J'ai peu de lumière chez moi, quelle plante choisir ?",
        "Le Sansevieria et le Zamioculcas sont d'excellents choix pour les endroits avec peu de lumière. Le Dracaena fragrans aussi.",
        "Comment entretenir un Ficus Lyrata ?",
        "Le Ficus Lyrata aime beaucoup la lumière indirecte. Arrosez-le quand la terre est sèche en surface et évitez les courants d'air.",
        "A quelle fréquence dois-je arroser mon cactus ?",
        "Les cactus ont besoin de peu d'eau. En général, un arrosage toutes les 2 à 4 semaines est suffisant, mais laissez bien la terre sécher entre deux arrosages.",
        "Est-ce que le Monstera Deliciosa est toxique pour les chats ?",
        "Oui, le Monstera Deliciosa est toxique pour les chats et les chiens s'ils en mangent. Il vaut mieux le placer hors de leur portée.",
        "Je cherche une plante qui fleurit en hiver.",
        "Le Schlumbergera, aussi appelé cactus de Noël, est une excellente plante qui fleurit en hiver. Le Cyclamen aussi.",
        "Comment savoir si ma plante a soif ?",
        "Vous pouvez toucher la terre. Si elle est sèche sur quelques centimètres de profondeur, c'est généralement le bon moment pour arroser. Les feuilles peuvent aussi paraître un peu molles.",
        "Qu'est-ce qu'un anthurium?",
        "L'anthurium est une plante d'intérieur populaire, connue pour ses 'fleurs' colorées qui sont en réalité des spathes. Elle aime l'humidité et la lumière vive mais indirecte.",
        "Comment prendre soin d'un anthurium?",
        "Pour un anthurium, maintenez le sol humide mais pas détrempé. Placez-le dans un endroit avec une lumière indirecte et une bonne humidité. Fertilisez toutes les 6-8 semaines au printemps et en été.",
        "Quelle est la meilleure plante pour purifier l'air?",
        "Le Spathiphyllum (Fleur de lune) est l'une des meilleures plantes pour purifier l'air. Le Sansevieria et le Chlorophytum comosum (plante araignée) sont aussi très efficaces.",
        "Je veux une plante facile à entretenir.",
        "Le Zamioculcas (plante ZZ) est extrêmement facile à entretenir. Il tolère une faible luminosité et des arrosages irréguliers. C'est parfait si vous n'avez pas beaucoup de temps.",
    ]
    trainer.train(plantes_conversations)

# Fonction d'entrainement sur les maths
def entrainer_sur_maths():
    trainer = ListTrainer(chazam_bot)
    math_conversations = [
        "Peux-tu calculer quelque chose pour moi ?",
        "Bien sûr ! Posez-moi une question mathématique.",
        "Que fait 10+10 ?",
        "10+10 = 20"
    ]
    trainer.train(math_conversations)

def demarrer_chat():
    print("Interface de chat activée. Tapez 'quitter' pour fermer.")
    while True:
        try:
            entree_utilisateur = input("Utilisateur : ")
            if entree_utilisateur.lower() == "quitter":
                break
            
            reponse = chazam_bot.get_response(entree_utilisateur)
            print(f"Chazam : {reponse}")

        except (KeyboardInterrupt, EOFError, SystemExit):
            break

if __name__ == "__main__":
    # Entrainement du chatbot
    print("Entraînement du chatbot...")
    entrainer_base()
    entrainer_sur_plantes()
    entrainer_sur_maths()
    print("Entraînement terminé.")
    
    demarrer_chat()