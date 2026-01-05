def analyze_footprint(username, birth_year, interests):
  risks=[]
  if len(username)<5:
    risk.append("Short username may be easy to guess or brute-force.")
  if birth_year.isdigit():
    age = 2025-int(birth_year)
    if age < 18:
      risks.append("User may be a minor — increased privacy risks.")
    else:
      risks.append("Age can be approximately inferred from public data.")
  common_interests=["gaming", "music", "coding", "art", "travel"]
  for interest in interests:
    if interest.lower() in common_interests:
      risks.append(
        f"Interest '{interest}' can be used for social engineering attacks."
            )
  return risks
print("=== Digital Footprint Simulator ===")
print("This tool demonstrates what could be inferred from shared data.\n")
username = input("Enter a username: ")
birth_year = input("Enter year of birth: ")
interests_input = input("Enter interests (comma separated): ")
interests=[i.strip() for i in interests_input.split(",")]

results = analyze_footprint(username, birth_year, interests)

print("\nPotential inferences and risks:")
if results:
  for r in results:
    print("-", r)
else:
  print("No significant risks detected.")
        
