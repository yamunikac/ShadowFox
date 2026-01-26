justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman"]
print(len(justice_league))

justice_league.append("Batgirl")
justice_league.append("Nightwing")
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

justice_league.sort()
print(justice_league)