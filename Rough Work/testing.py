import random

def roulette_wheel(chromosome_number, fitness_quality):
    total_length = len(fitness_quality)
    fitness_probability = [(i/sum(fitness_quality)) for i in fitness_quality]
    print(f'Fitness Probability: {fitness_probability}')
    
    sample = random.uniform(0,1)
    # sample = 0.78

    cummulative = 0

    species_chromosome_probability = []

    for i in range(total_length):
        cummulative += fitness_probability[i]
    
        if sample <= cummulative:
            species_chromosome_probability.append(chromosome_number[i])
    print(sample)
    # print(species_chromosome_probability)
    return [species_chromosome_probability[-1]]


chromosome_number = [1,2,3,4,5]
fitness_quality = [18,8,39,21,14]

# print(f"chromosome number: {chromosome_number}")
# print(f"fitness quality: {fitness_quality}")


count_dictionary = {1:0,2:0,3:0,4:0,5:0}

for _ in range(10):
    species_chromosome_values = roulette_wheel(chromosome_number,fitness_quality)
    for i in chromosome_number:
        count = species_chromosome_values.count(i)
        count_dictionary[i] += count
print(count_dictionary)

print(sum(count_dictionary.values()))