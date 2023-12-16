const fs = require('fs');

let path = fs.readFileSync('input.txt', 'utf8').split('\n');

let checkPath = (xAxisChange, yAxisChange) => {
    let trees = 0;
    let currentLoc = [0, 0];
    let matrix = path.map(row => row.split(''));

    while (currentLoc[0] < matrix.length) {
        if (matrix[currentLoc[0]][currentLoc[1]] === '#') {
            trees++;
        }

        currentLoc[0] = currentLoc[0] + yAxisChange;
        currentLoc[1] = currentLoc[1] + xAxisChange;

        if (matrix[currentLoc[0]]) {
            if (currentLoc[1] >= matrix[currentLoc[0]].length) {
                currentLoc[1] = (currentLoc[1] - matrix[currentLoc[0]].length);
            }
        }
    }

    console.log("Trees: ", trees);
    return trees
}

const multiple = checkPath(1, 1) * checkPath(3, 1) * checkPath(5, 1) * checkPath(7, 1) * checkPath(1, 2);

console.log(multiple);