# Practice 
##if statement
##counties = ["Arapahoe", "Denver", "Jefferson"]
##if counties[1] == 'Denver':
##    print(counties[1])

##if counties[3] != 'Jefferson':
##    print(counties[2])


## if-else statement
## temperature = int(input("What is the temperature outside?"))
##if temperature > 80:
##    print("Turn on the AC")
##else:
##    print("Open the windows")

## Nested If-Else Statement
# What is the score?
# score = int(input("What is your test score?"))

# Determine the grade.
##if score >= 90:
##    print('Your grade is an A')
##else:
##    if score >= 80:
##        print('Your grade is a B')
##    else:
##        if score >= 70:
##            print('Your grade is a C')
##        else:
##            if score >= 60:
##                print('Your grade is a D')
##            else:
##                print('Your grade is an F')

# Practice membership operation
##counties = ["Arapahoe","Denver","Jefferson"]
##if "El Paso" in counties:
##    print("El Paso is in the list of counties.")
##else:
##    print("El Paso is not the list of counties.")

# Practice logical operation - AND
##if "Arapahoe" in counties and "El Paso" in counties:
##    print("Arapahoe and El Paso are in the list of counties.")
##else:
##    print("Arapahoe or El Paso is not the list of counties.")

# Practice logical operation - OR
##if "Arapahoe" in counties or "El Paso" in counties:
##    print("Arapahoe or El Paso is in the list of counties.")
##else:
##    print("Arapahoe and El Paso is not the list of counties.")

# Practice logical operation - NOT
##if "Arapahoe" in counties and "El Paso" not in counties:
##   print("Only Arapahoe is in the list of counties.")
##else:
##    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# Practice For Loops
##for county in counties:
##    print(county)

# Practice Range()
##numbers = [0, 1, 2, 3, 4]
##for num in numbers:
##    print(num)
##for num in range(5):
##    print(num)

# indexing iterate through a list 
# - if the list contains string, we'll need to get the length as an integer
##for i in range(len(counties)):
##    print(counties[i])

# Practice Dictionary - Key and Value
## Interate through a Dictionary - Get the keys
##counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

##for county in counties_dict:
##    print(county)

## Get the values
##for voters in counties_dict.values():
##    print(voters)

## Get values - format dictionary_name[key]
##for county in counties_dict:
##    print(counties_dict[county])

## Get values - format get()
##for county in counties_dict:
##    print(counties_dict.get(county))

## Get the Key-Value Pairs of a Dictionary
##for county, voters in counties_dict.items():
##    print(county,voters)

# Iterate Through a list of dictionary
## Get each dictionary in a list of dictionary
##voting_data = [{"county":"Arapahoe",  "registered_voters": 422829},
##               {"county":"Denver",    "registered_voters": 463353},
##               {"county":"Jefferson", "registered_voters": 432438}]

##for county_dict in voting_data:
##    print(county_dict)
## using Range() to print county
##for i in range(len(voting_data)):
##    print(voting_data[i]['county'])

## Get values from a list of dictionary
##for county_dict in voting_data:
##    for value in county_dict.values():
##        print(value)

##for county_dict in voting_data:
##    print(county_dict['registered_voters'])

# F-strings: Formatted String Literals
## Original code
##my_votes = int(input("How many votes did you get in the election? "))
##total_votes = int(input("What is the total votes in the election? "))
##percentage_votes = (my_votes / total_votes) * 100
##print("I received " + str(percentage_votes)+"% of the total votes.")

## Formatted code
##my_votes = int(input("How many votes did you get in the election? "))
##total_votes = int(input("What is the total votes in the election? "))
##print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# Using F-Strings with Dictionaries
##counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
##for county, voters in counties_dict.items():
##    print(county + " county has " + str(voters) + " registered voters.")

## using f-string
##for county, voters in counties_dict.items():
##    print(f"{county} county has {voters} registered voters.")

# Multiline F-Strings
##candidate_votes = int(input("How many votes did the candidate get in the election? "))
##total_votes = int(input("What is the total number of votes in the election? "))

### Original
##message_to_candidate = (
##    f"You received {candidate_votes} number of votes. "
##    f"The total number of votes in the election was {total_votes}. "
##    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

###Format Floating-Point Decimals
##message_to_candidate = (
##    f"You received {candidate_votes:,} number of votes. "
##    f"The total number of votes in the election was {total_votes:,}. "
##    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

##print(message_to_candidate) 

# Module 3.2.11 - Skill Drill
##counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
##for county, voters in counties_dict.items():
##   print(f"{county} county has {voters} registered voters")


# Module 3.2.11 - Skill Drill
voting_data = [{"county":"Arapahoe",  "registered_voters": 422829},
               {"county":"Denver",    "registered_voters": 463353},
               {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)
    for county, registered_voters in county_dict.items():
        print(county, registered_voters)
##        print(f"{county} county has {registered_voters} registered voters" )
        

