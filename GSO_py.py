#GSO_git

skra = input("Sláðu inn nafn á skrá ")
nafnskra = skra+".txt"
skrainMin = open(nafnskra, "w+")
skrainMin.write("Fyrsta línan í skránni" + "\n")
skrainMin.close()
skrainMin = open(nafnskra, "a")
lina1 = input("Fyrsta linan" + "\n")
lina2 = input("Önnur linan" + "\n")
lina3 = input("Þriðja linan" + "\n")
skrainMin.write(lina1 + "\n")
skrainMin.write(lina2 + "\n")
skrainMin.write(lina3 + "\n")
skrainMin = open(nafnskra, "r")
print(skrainMin.read())
skrainMin.close()