# Your Place in the Universe Program

# This program will determine the approximate number of atoms that a person is
# person consists of and the percent of the universe that they comprise

# Initialization
num_atoms_universe = 10e80
weight_avg_person = 70  # 70 kg (154 lbs)
num_atoms_avg_person = 7e27

# Program greeting
print('This program will determine your place in the universe.')

# Prompt for user's weight
weight_lbs = int(input('Enter your weight in pounds: '))

# Convert weight to kilograms
weight_kg = 2.2 * weight_lbs

# Determine number atoms and percentage of universe
num_atoms = (weight_kg / weight_avg_person) * num_atoms_avg_person
percent_of_universe = (num_atoms / num_atoms_universe) * 100

# Display results
print('You contain approximately', format(num_atoms, '.2e'), 'atoms')
print('Therefore, you comprise', format(percent_of_universe, '.2e'),
      '% of the universe')

