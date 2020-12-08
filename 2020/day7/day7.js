const fs = require('fs');

let input = fs.readFileSync('input.txt', 'utf8').split('\n');

const analyzeBagRules = () => {

    let holdsGoldBag = [];
    let ruleSet = {};
    input.forEach(rule => {
        let key = rule.split('contain')[0];
        let bagsInside = rule.split('contain')[1].split(',');
        ruleSet[key.trim()] = formatBagsInside(bagsInside);
    });

    fs.writeFile('ruleSet.js', JSON.stringify(ruleSet), () => console.log("done"));

    let checkBags = (key, bags) => {
        if (bags.includes('shiny gold bag') || bags.includes('shiny gold bags')) {
            if (!holdsGoldBag.includes(key)) {
                holdsGoldBag.push(key);
            }
            return true;
        } else if (bags.includes('no other bags')) {
            return false;
        } else {
            bags.forEach(bag => {
                let bagName = bag;
                if (bag.charAt(bag.length - 1) !== 's') {
                    bagName = `${bag}s`;
                }

                if (checkBags(bagName, ruleSet[bagName])) {
                    if (!holdsGoldBag.includes(key)) {
                        holdsGoldBag.push(key);
                    }
                    return true;
                } else {
                    return false;
                }
            })
        }
    }

    Object.keys(ruleSet).forEach(key => {
        checkBags(key, ruleSet[key]);
    });

    console.log(holdsGoldBag);
    console.log(holdsGoldBag.length);

    fs.writeFile('results.js', JSON.stringify(holdsGoldBag), () => console.log("done"));

    console.log(Object.keys(ruleSet).length);
}


let formatBagsInside = (bagsInside) => {
    let bags = bagsInside.map(bag => {
        return bag.replace(/[0-9.]/g, '').trim();
    })

    return bags;
}

analyzeBagRules();