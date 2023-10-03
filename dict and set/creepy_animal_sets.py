scorpions = {"emperor", "red claw", "arizona", "forest", "fat tail"}
snakes = {"python", "cobra", "viper", "anaconda", "mamba"}
spiders = {"tarantula", "black widow", "wolf spider", "crab spider"}
vespas = {"yellow jacket", "hornet", "paper wasp"}

things_that_sting = scorpions | vespas
print(things_that_sting)

arachnids = scorpions.union(spiders)
print(arachnids)
