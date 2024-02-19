import csv

def translations(filename):
    number_to_turkana = {}
    turkana_to_number = {}
    
#defining the values in the csv file 
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
           number = int(row[0])
           turkana_word = (row[1])
           number_to_turkana[number] = turkana_word
           turkana_to_number[turkana_word] = number
        
    return number_to_turkana, turkana_to_number

# function that defines how to translate a number to turkana language       
def translate_to_turkana(number):
    number_to_turkana, _ = translations('project.csv')

    if number in number_to_turkana:
        return number_to_turkana[number]

# divided number into tens and ones 
    tens_digit = number // 10
    ones_digit = number % 10

# this block intends to combine a number in tens value with a ones value eg 23 , 91 
    if tens_digit in number_to_turkana and ones_digit in number_to_turkana:
        tens_translation = number_to_turkana[tens_digit * 10]
        ones_translation = number_to_turkana[ones_digit]
        return tens_translation + " " + ones_translation
    else:
        return "Number out of range"
        
# translate a word in Turkana language to corresponding number           
def translate_to_number(word):
    _ , turkana_to_number = translations('project.csv')
    
    if word in turkana_to_number:
        return turkana_to_number[word]
    else:
        return "Word Not In Turkana Language"
    
while True:
    print("Options")
    print("1. Translate number to Turkana")
    print("2. Translate Turkana to number")
    print("3. Exit")  
    
    choice = int(input("Enter your choice(1/2/3): "))
    
    if choice == 1:
        number = int(input("Enter a number (0-#): "))
        translations_number = translate_to_turkana(number)
        print(f"The Number {number} in Turkana is: {translations_number}")
    if choice == 2:
        #word = input("Enter a number in Turkana language: ")
        word = str(input("Enter the Turkana Word(): "))
        translations_turkana = translate_to_number(word)
        print(f"The Turkana Word  {word} corresponds to: {translations_turkana}")
    if choice == 3:
        print("Exiting ...")
        break
    else:
        print("Enter a valid option")
        
        
        
            
     
    
          
        