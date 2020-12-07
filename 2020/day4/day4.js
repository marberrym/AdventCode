const fs = require('fs');

let input = fs.readFileSync('input.txt', 'utf8').split('\n\n');
let validEyeColors = [ "amb", "blu", "brn", "gry", "grn", "hzl", "oth" ];

const isNumeric = (str) => {
    if (typeof str != "string") return false
    return !isNaN(str) && !isNaN(parseFloat(str))
}

const checkPassports = () => {
    let validPassports = 0;

    let passports = input.map(cred => {
        return cred.replace(/\n/g, " ").split(" ");
    })

    passports.forEach(passport => {
        let passportCreds = {
            byr : false,
            iyr:  false,
            eyr : false,
            hgt : false,
            hcl : false,
            ecl : false,
            pid : false,
            cid : false,
        }

        passport.forEach(line => {
            let type = line.split(":")[0];
            let input = line.split(":")[1];

            if (checkValidity(type, input)) {
                passportCreds[type] = true;
            }
        })

        let isValidPassport =
            passportCreds.byr &&
            passportCreds.iyr &&
            passportCreds.eyr &&
            passportCreds.hgt &&
            passportCreds.hcl &&
            passportCreds.ecl &&
            passportCreds.pid;

        if (isValidPassport) {
            validPassports++;
        }
    });

    console.log("Valid Passport Count: ", validPassports);
    return validPassports;
}

let checkYear = (minYear, maxYear, input) => input.match(/[0-9]{4}/g) && input.length === 4 && input >= minYear && input <= maxYear;

let checkEyeColor = (input) => validEyeColors.includes(input);

let checkHairColor = (input) => input.match(/#[0-9a-zA-Z]{6}/g);

let checkPID = (input) => isNumeric(input) && input.length === 9;

let checkHeight = (input) => {
    if (input.match(/[0-9]{2,3}(cm|in)/g)) {
        if (input.slice(-2) === 'in') {
            let number = input.replace("in", "");
            if (number >= 59 && number <= 76) {
                return true;
            } else {
                return false;
            }
        } else if (input.slice(-2) === 'cm') {
            let number = input.replace("cm", "");
            if (number >= 150 && number <= 193) {
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    } else {
        return false;
    }

}

let checkValidity = (type, input) => {
    switch(type) {
        case "byr":
            return checkYear(1920, 2002, input);
        case "iyr":
            return checkYear(2010, 2020, input);
        case "eyr":
            return checkYear(2020, 2030, input);
        case "hgt":
            return checkHeight(input);
        case "hcl":
            return checkHairColor(input);
        case "ecl":
            return checkEyeColor(input);
        case "pid":
            return checkPID(input);
        case "cid":
            return true;
        default:
            return false;
    }
}

checkPassports();