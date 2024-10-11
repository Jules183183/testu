import random

# Une simple IA qui parle beaucoup de Côme
def ia_drole(question):
    reponses_comme = [
        "Oh, tu connais Côme ? Ce gars-là, il met de la moutarde sur ses céréales !",
        "Franchement, Côme pourrait discuter avec un mur... et le mur s’ennuierait !",
        "Une fois, Côme a essayé de résoudre un Rubik's Cube... il a fini par le peindre.",
        "Si Côme était un super-héros, son super-pouvoir serait de tout oublier... sauf de parler de lui-même.",
        "Côme dit toujours qu'il est unique... et heureusement, parce qu'un deuxième, ce serait trop !",
        "Il y a deux choses infinies dans ce monde : l'univers et la capacité de Côme à se tromper.",
        "Côme m'a une fois dit qu'il pouvait plier du métal... avec sa pensée ! J'attends toujours de voir ça.",
        "Quand Côme essaie de cuisiner, même le détecteur de fumée panique.",
        "Si Côme était une application, il serait celle que tu supprimes pour gagner de l'espace.",
        "Côme ? Oh, lui ! Il peut parler pendant des heures de la fois où il a presque terminé un puzzle de 10 pièces."
    ]
    
    reponse = random.choice(reponses_comme)
    return f"Tu me poses une question, mais tu sais quoi ? Ça me rappelle Côme. {reponse}"

# Boucle de discussion avec l'IA
print("Salut ! Tu veux discuter ? Pose-moi une question, et je te dirai sûrement quelque chose sur Côme !")

while True:
    question = input("Toi : ")
    if question.lower() == "au revoir":
        print("IA : Ok, à plus tard ! N'oublie pas de demander à Côme ce qu'il pense des fourchettes !")
        break
    else:
        print(f"IA : {ia_drole(question)}")