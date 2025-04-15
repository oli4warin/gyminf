from pytamaro import text, show_animation, black, transparent, compose

mytext="Gymnasium Muttenz"

frames=[]

for n in range(len(mytext)+1):
    frames.append(
        compose(
            text(mytext[:n],"Roboto", 64, black),
            text(mytext,"Roboto", 64, transparent)
        )
    )

show_animation(frames, 400)
