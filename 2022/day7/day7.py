f = open('input.txt', 'r');
input = f.read().splitlines();
tf = open('testCase.txt', 'r');
test = tf.read().splitlines();



def main(input):
    homeDirectory = {}
    lastCommand = ''
    lastDirectoryEntered = ''
    pwd = '/'

    for command in input:
        currentDirectory = None

        commandPieces = command.split(' ');
        print(command)
        if commandPieces[0] == '$':
            lastCommand = command
        
        if lastCommand == "$ ls" and commandPieces[0] != '$':
            activePath = []

            if pwd != '/':
                activePath = list(filter(None, pwd.split('/')))
                print(activePath)
            
            if len(activePath) > 0:
                while len(activePath) > 0:
                    print("we have sub dirs")
                    if currentDirectory is None:
                        currentDirectory = homeDirectory[activePath[0]]
                    else:
                        currentDirectory = currentDirectory[activePath[0]]

                    print(currentDirectory)
                    print(activePath[0])
                    activePath.pop(0)
            
            if commandPieces[0] == 'dir': 
                if currentDirectory is not None:
                    currentDirectory[commandPieces[1]] = {}
                else:       
                    homeDirectory[commandPieces[1]] = {}
            else:
                if currentDirectory is not None:
                    currentDirectory[commandPieces[1]] = commandPieces[0]
                else:
                    homeDirectory[commandPieces[1]] = commandPieces[0]

        if commandPieces[0] == '$' and commandPieces[1] == "cd":
            print("directory change")
            if commandPieces[2] == '/':
                pwd = '/'
            elif commandPieces[2] == '..':
                pwd = pwd[:-len(lastDirectoryEntered)]
                
            else:
                pwd = f"{pwd}{commandPieces[2]}/"
                lastDirectoryEntered = f"{commandPieces[2]}/"
    
    print(homeDirectory)

main(test)
