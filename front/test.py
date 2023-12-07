from fish import Fish
fish = Fish("./crop_labeled.csv", 150, 3000, 0.7)
print(fish.predict('fishy2.png'))
