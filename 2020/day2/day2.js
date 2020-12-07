const fs = require('fs');

let passwordList = fs.readFileSync('input.txt', 'utf8').split('\n');

// console.log(passwordList,"readMe");

let checkValidPasswords = () => {
    let validPasswords = 0;

    passwordList.forEach(passwordParams => {
        let protocolMinimum = passwordParams.split(":")[0].split(" ")[0].split("-")[0];
        let protocolMaximum = passwordParams.split(":")[0].split(" ")[0].split("-")[1];
        let target = passwordParams.split(":")[0].split(" ")[1];
        let passwordString = passwordParams.split(":")[1];

        if (checkForCharExistence2(protocolMinimum, protocolMaximum, target, passwordString)) {
            console.log("Password valid!");
            validPasswords++;
        } else {
            console.log("Password invalid! :(")
        }
    })
    return validPasswords;
}

// part 1
let checkForCharExistence = (minimum, maximum, character, string) => {
    let count = 0;
    [...string].forEach(char => {
        if (char === character) {
            count++;
        }
    })

    if (count <= maximum && count >= minimum) {
        return true;
    } else {
        return false;
    }
}

//part 2
let checkForCharExistence2 = (firstIndex, secondIndex, character, string) => {
    let firstPos = firstIndex - 1;
    let secondPos = secondIndex - 1;

    let count = 0;

    if (string.trim().charAt(firstPos) === character) {
        count++;
    }

    if (string.trim().charAt(secondPos) === character) {
        count++;
    }


    if (count === 1) {
        return true;
    }

    return false;
}

console.log(checkValidPasswords());