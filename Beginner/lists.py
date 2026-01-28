justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Members count:", len(justice_league))

justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("After adding members:", justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Leader changed:", justice_league)

justice_league.remove("Flash")
justice_league.insert(justice_league.index("Aquaman") + 1, "Green Lantern")
justice_league.insert(justice_league.index("Green Lantern") + 1, "Flash")
print("After resolving conflict:", justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
justice_league.sort()
print("Final sorted team:", justice_league)
