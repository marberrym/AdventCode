const fs = require('fs');

let input = fs.readFileSync('input.txt', 'utf8').split('\n');

const analyzeTickets = () => {
    let maximumSeatId = -Infinity;
    let claimedSeatIds = [];

    input.forEach(ticket => {
        let rowRange = [0, 127];
        let row;
        let columnRange = [0, 7];
        let column;
        let seatId;

        for(x=0; x<ticket.length; x++) {
            if (x < 7) {
                if (rowRange[1] - rowRange[0] === 1) {
                    row = findSelection(ticket[x], rowRange);
                } else {
                    rowRange = splitRange(ticket[x], rowRange);
                }
            } else {
                if (columnRange[1] - columnRange[0] === 1) {
                    column = findSelection(ticket[x], columnRange);
                } else {
                    columnRange = splitRange(ticket[x], columnRange);
                }
            }
        }

        seatId = setSeatId(row, column);

        if (seatId > maximumSeatId) {
            maximumSeatId = seatId;
        }

        claimedSeatIds.push(seatId);

    });

    console.log("Maximum seat id is... ", maximumSeatId);
    findMySeat(claimedSeatIds);
}

const setSeatId = (row, column) => {
    return (row * 8) + column;
}

const splitRange = (direction, range) => {
    const newRange = [0, 0];
    if (direction === 'F' || direction === 'L') {
        let topChange = Math.round((range[1] - range[0])/ 2);
        newRange[0] = range[0];
        newRange[1] = range[1] - topChange;
        return newRange;
    } else if (direction === 'B' || direction === 'R') {
        let bottomChange = Math.round((range[1] - range[0])/ 2);
        newRange[0] = range[0] + bottomChange;
        newRange[1] = range[1];
        return newRange;
    }
}

const findSelection = (direction, range) => {
    if (direction === 'F' || direction === 'L') {
        return range[0];
    } else if (direction === 'B' || direction === 'R') {
        return range[1];
    }
}

const findMySeat = (claimedSeats) => {
    unclaimedSeats = [];
    let mySeat;

    claimedSeats.forEach(seat => {
        if (!claimedSeats.includes(seat + 1)) {
            unclaimedSeats.push(seat + 1);
        } else if (!claimedSeats.includes(seat - 1)) {
            unclaimedSeats.push(seat - 1);
        }
    });

    unclaimedSeats.forEach(seat => {
        if (unclaimedSeats.filter(checkedSeat => checkedSeat === seat).length > 1) {
            mySeat = seat;
        }
    });

    console.log("My seat is ... ", mySeat);
}

analyzeTickets();