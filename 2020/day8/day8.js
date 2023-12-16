const fs = require('fs');

let input = fs.readFileSync('input.txt', 'utf8').split('\n');

const executeCommand = (ins, acc, rip) => {
    const [opcode, arg ] = ins.split(' ');

    if (opcode === 'nop') {
        rip += 1;
        return {
            acc,
            rip
        }
    } else if (opcode === 'jmp') {
        rip += Number(arg);
        return {
            acc,
            rip,
        }
    } else if (opcode === 'acc') {
        acc += Number(arg);
        rip += 1;
        return {
            acc,
            rip,
        }
    }
}

const analyzeStartCode = () => {
    let seen = [];
    let accValue = 0;
    let rip = 0

    for (i in input) {
        seen.push(false);
    }


    while (true) {
        if (seen[rip] === true) {
            break;
        } else {
            seen[rip] = true;
            let resp = executeCommand(input[rip], accValue, rip);
            accValue = resp.acc;
            rip = resp.rip;
        }
    }

    console.log(accValue);
}

// analyzeStartCode();


// Part 2:


let analyzePartTwo = () => {
    for(let x in input) {
        let acc = 0;
        let rip = 0;
        let seen = [];

        let command = input[x].split(" ")[0];
        let parameter = input[x].split(" ")[1];

        if (command === 'jmp') {
            command = 'nop';
        } else if (command === 'nop') {
            command = 'jmp'
        }

        let patch_n = x;
        let patch = `${command} ${parameter}`;

        console.log("X/Patch is...", x, patch_n);

        for(let x in input) {
            seen.push(false);
        }

        try {
            while (true) {
                console.log("Rip is...", rip);
                if (seen[rip] === true) {
                    break;
                }
                seen[rip] = true;
                let ins = input[rip];

                if (rip == patch_n) {
                    console.log("patching...")
                    ins = patch;
                }

                let resp = executeCommand(ins, acc, rip);
                acc = resp.acc;
                rip = resp.rip;
            }

        } catch (error) {
            console.log("I make it here...")
            console.log(error);
            console.log(acc)
            break;
        }
    }
}

analyzePartTwo();