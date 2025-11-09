import os
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import random

def explore(root, seed):
    random.seed(seed)
    classes = [d for d in os.listdir(root) if not d.startswith('.')]
    print(f"Liczba klas: {len(classes)}" + f"\n\nKlasy: {classes}")

    summary = []
    print("\nPodgląd kilku losowych obrazów (trzy z każdej klasy z czego po jednym z każdego typu:)\n")
    for c in classes:
        class_path = os.path.join(root, c)
        files = os.listdir(class_path)
        images = [f for f in files if f.endswith(('.jpg', '.png', '.jpeg'))]

        total = len(images)
        digital = [i for i in images if i.startswith('digit')]
        drawn = [i for i in images if i.startswith('drawn')]
        stamp = [i for i in images if i.startswith('stamp')]


        img1 = os.path.join(class_path, random.choice(digital))
        img2 = os.path.join(class_path, random.choice(drawn))
        img3 = os.path.join(class_path, random.choice(stamp))
        fig, ax = plt.subplots(1, 3, figsize=(9, 3))
        for ax, path in zip(ax, [img1, img2, img3]):
            img = Image.open(path).convert('RGB')
            ax.imshow(img)
            w, h = img.size
            ax.set_title(f"Class: {c}\n"
                         f"Type: {path.split('\\')[-1][:-6]}\n"
                         f"Size: {w}x{h}")
            ax.axis('off')
        plt.show()


        summary.append({"class": c,
                        "size": total,
                        "digital": len(digital),
                        "drawn": len(drawn),
                        "stamp": len(stamp)})


    dataframe = pd.DataFrame(summary)
    print(f"\nPodsumowanie danych: \n{dataframe}")

    return classes

