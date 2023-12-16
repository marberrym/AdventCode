const console = require("console");

let originalOpCodes = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,10,31,35,2,6,35,39,1,39,13,43,1,43,9,47,2,47,10,51,1,5,51,55,1,55,10,59,2,59,6,63,2,6,63,67,1,5,67,71,2,9,71,75,1,75,6,79,1,6,79,83,2,83,9,87,2,87,13,91,1,10,91,95,1,95,13,99,2,13,99,103,1,103,10,107,2,107,10,111,1,111,9,115,1,115,2,119,1,9,119,0,99,2,0,14,0];

let executeCode = (originalOpCodes) => {
    let index = 0;
    let opCodes = originalOpCodes;

    for(x=0; x<=99; x++) {
        opCodes[1] = x;
        console.log(opCodes[1]);
        for(y=0; y<=99; y++) {
            opCodes[2] = y;
            console.log(opCodes[2]);
            while (index <= opCodes.length) {
                if (opCodes[index] === 1) {
                    let targetPosition = opCodes[index + 3];
                    let firstIntPosition = opCodes[index + 1];
                    let secondIntPosition = opCodes[index + 2];

                    opCodes[targetPosition] = opCodes[firstIntPosition] + opCodes[secondIntPosition];
                    index += 4;
                } else if (opCodes[index] === 2) {
                    let targetPosition = opCodes[index + 3];
                    let firstIntPosition = opCodes[index + 1];
                    let secondIntPosition = opCodes[index + 2];

                    opCodes[targetPosition] = opCodes[firstIntPosition] * opCodes[secondIntPosition];
                    index += 4;
                } else if (opCodes[index] === 99) {
                    let output = opCodes[0];
                    if (output === 19690720) {
                        console.log("Answer found")
                        return {
                            output: output,
                            x: x,
                            y: y,
                        }
                        break;
                    } else {
                        console.log(opCodes[0]);
                        opCodes = originalOpCodes;
                        break;
                    }
                } else {
                    "Invalid opcode"
                    index += 4;
                }
            }
        }
    }
}

executeCode(originalOpCodes);