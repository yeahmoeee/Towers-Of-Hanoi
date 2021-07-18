from stack import Stack

left_stack = Stack()
middle_stack = Stack()
right_stack = Stack()

disks_input = int(input("How many disks do you want to start with? ")) 

for i in range(disks_input, 0, -1):
    left_stack.push(i) 


stacks = [left_stack, middle_stack, right_stack]

#moving everything from left_stack to right_stack
stack_names_list = ["Left stacks: ","Middle stacks: ","Right stacks: "]
stack_names = {"l":left_stack,"m":middle_stack,"r":right_stack}



num_moves = 0 
while right_stack.size != disks_input:
    for i in range(len(stacks)): 
        print("\n" + stack_names_list[i])
        print(stacks[i])
    move_from = input("Enter the stack you want to move from: ")
    move_to = input("Enter the stack you want to move to: ")
    if move_from != move_to:
        if stack_names[move_from].size != 0:
            if stack_names[move_to].size == 0:
                stack_names[move_to].push(stack_names[move_from].pop())
            else:
                if stack_names[move_to].peek() > stack_names[move_from].peek():
                    stack_names[move_to].push(stack_names[move_from].pop())
                elif stack_names[move_to].peek() < stack_names[move_from].peek():
                    print("\nInvalid move.") 
        else:
            print("\nStack to move from is empty.") 
        
    else:
        print("\nInvalid move.")
    num_moves += 1

for i in range(len(stacks)): 
        print("\n" + stack_names_list[i])
        print(stacks[i])
print("\nIt took you " + str(num_moves) + " steps to finish the game.")