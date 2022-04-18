file = open("/Users/rajat/Documents/Uni/SER502/SER502-Spring2022-Team7/src/test.txt", "r")
sample = file.read()

keywords = ["for"]
keywords_language = ["shuru"]
specials = set(["=", "+", "-", "}", ",", "{", "/", ";", "\\", "(", ")", "<", ">", ":" ])

stack = []
final_stack = []
x = 0

def tokenise(sample):
    x = 0
    i = 0
    stack = []
    
    while(i < len(sample)):

        #Example: Sup world
        if sample[i] == " " or sample[i] == "\n" and sample[i - 1] not in specials and sample[x+1:i] not in keywords:
            stack.append(sample[x:i])
            x = i + 1
            i += 1
            continue

        # Example: "Hello, world! :)" (String)
        elif sample[i] == '"':
            stack.append(sample[i])

            for j in range(i + 1, len(sample)):
                
                if sample[j] == '"':
                    new_string = sample[i+1:j]
                    substring_length = len(new_string)
                    break

            k = 0
            for l in range(len(new_string)):
                if new_string[l] == " ":
                    stack.append(new_string[k:l])
                    k = l + 1

                elif l == len(new_string) - 1:
                    stack.append(new_string[k:l+1]) 

            stack.append('"')
            i += substring_length + 2
            x = i + 1
            continue

        #Example: for-loop()
        elif sample[x:i] == "for-loop":
            stack.append(sample[x+1:i])
            x = i + 1
            i += 1
            continue   
        
        #Example: i=
        elif sample[i] in specials and sample[i - 1] not in specials and sample[x+1:i] not in keywords:
            stack.append(sample[x:i])        
            stack.append(sample[i])
            x = i + 1
            i += 1
            continue
        
        #Example: ++
        elif sample[i] in specials and sample[x+1:i] not in keywords:
            stack.append(sample[i])
            x = i + 1
            i += 1
            continue

        else:
            i += 1
            continue

    return stack

for new_line in tokenise(sample):
    final_stack.append(new_line.replace("\n", ""))

while("" in final_stack):
    final_stack.remove("")

print(final_stack)