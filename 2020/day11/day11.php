<?php
/**
 * Solves day 9 algorithm for advent of code
 *
 * PHP version 7
 *
 * @category Algorithm_Solution
 * @package  Advent_Code
 * @author   Author <marberrym@gmail.com>
 * @license  https://opensource.org/licenses/MIT MIT License
 * @link     http://localhost/
 */

$data = prepData();

$testCase = array(
    str_split("L.LL.LL.LL"),
    str_split("LLLLLLL.LL"),
    str_split("L.L.L..L.."),
    str_split("LLLL.LL.LL"),
    str_split("L.LL.LL.LL"),
    str_split("L.LLLLL.LL"),
    str_split("..L.L....."),
    str_split("LLLLLLLLLL"),
    str_split("L.LLLLLL.L"),
    str_split("L.LLLLL.LL"),

);

// $patOneSolution = solvePartOne($testCase);

/**
 * Prepares data for use in algorithm
 *
 * @return array
 */
function prepData()
{
    $file="input.txt";
    $fopen = fopen($file, "read");
    $fread = fread($fopen, filesize($file));
    fclose($fopen);

    $splitBy = "\n";
    $split = explode($splitBy, $fread);

    $data = array();

    foreach ($split as $isle) {
        array_push($data, str_split($isle));
    };

    return $data;
}

function solvePartOne($data)
{
    $currentSeats = $data;
    $nextSeats = analyzeSeats($data);

    while ($currentSeats != $nextSeats) {
        $currentSeats = $nextSeats;
        $nextSeats = analyzeSeats($currentSeats);
    }

    $finalSeats = $currentSeats;

    // print_r($finalSeats);

    print_r(countSeats($finalSeats));

}

function analyzeSeats($data)
{
    $currentArrangement = $data;
    $returnArrangement = $data;

    for ($row=0; $row<count($currentArrangement); $row++) {
        $previousRow = $currentArrangement[$row - 1];
        $currentRow = $currentArrangement[$row];
        $nextRow = $currentArrangement[$row + 1];

        for ($col=0; $col<count($currentRow); $col++) {

            $currentSeat = $currentRow[$col];
            $adjacentSeats = findFirstSeatsInSight($row, $col, $currentArrangement);
            // getAdjacentSeats($previousRow, $currentRow, $nextRow, $col);

            if ($currentSeat == "L" && $adjacentSeats["#"] == 0) {
                $returnArrangement[$row][$col] = "#";
            } else if ($currentSeat == "#" && $adjacentSeats["#"] >= 5) {
                $returnArrangement[$row][$col]= "L";
            }
        }
    }

    // print_r($returnArrangement);

    return $returnArrangement;
}

function countSeats ($seatConfig)
{
    $unoccupiedSeats = 0;

    foreach ($seatConfig as $row) {
        $seats = array_count_values($row);
        $unoccupiedSeats += $seats["#"];
    }

    return $unoccupiedSeats;
}

function getAdjacentSeats($previousRow, $currentRow, $nextRow, $currentSeat) {
    $adjacentSeats = array(
        $previousRow[$currentSeat - 1],
        $previousRow[$currentSeat],
        $previousRow[$currentSeat + 1],
        $currentRow[$currentSeat - 1],
        $currentRow[$currentSeat + 1 ],
        $nextRow[$currentSeat - 1],
        $nextRow[$currentSeat],
        $nextRow[$currentSeat + 1],
    );

    $adjacentSeatValues = array_count_values($adjacentSeats);

    return $adjacentSeatValues;
}

function findFirstSeatsInSight($currentRow, $currentColumn, $data) {
    $adjacentSeats = array(
        getFirstSeatInSight("N", $currentRow, $currentColumn, $data),
        getFirstSeatInSight("NE", $currentRow, $currentColumn, $data),
        getFirstSeatInSight("E", $currentRow, $currentColumn, $data),
        getFirstSeatInSight("SE", $currentRow, $currentColumn, $data),
        getFirstSeatInSight("S", $currentRow, $currentColumn, $data),
        getFirstSeatInSight("SW", $currentRow, $currentColumn, $data),
        getFirstSeatInSight("W", $currentRow, $currentColumn, $data),
        getFirstSeatInSight("NW", $currentRow, $currentColumn, $data),
    );
    print_r($adjacentSeats);

    $adjacentSeatValues = array_count_values($adjacentSeats);

    return $adjacentSeatValues;

}

function getFirstSeatInSight($direction, $currentRow, $currentColumn, $currentArrangement)
{
    switch ($direction) {
    case "N":
        return checkDirection($currentRow, $currentColumn, $currentArrangement, 0, 1);
    case "NE":
        return checkDirection($currentRow, $currentColumn, $currentArrangement, 1, 1);
    case "E":
        return checkDirection($currentRow, $currentColumn, $currentArrangement, 1, 0);
    case "SE":
        return checkDirection($currentRow, $currentColumn, $currentArrangement, 1, -1);
    case "S":
        return checkDirection($currentRow, $currentColumn, $currentArrangement, 0, -1);
    case "SW":
        return checkDirection($currentRow, $currentColumn, $currentArrangement, -1, -1);
    case "W":
        return checkDirection($currentRow, $currentColumn, $currentArrangement, -1, 0);
    case "NW":
        return checkDirection($currentRow, $currentColumn, $currentArrangement, -1, 1);
    }
}

function checkDirection($currentRow, $currentColumn, $currentArrangement, $columnOffset, $rowOffset) {
    $checkedRow = $currentRow + $rowOffset;
    $checkedCol = $currentColumn + $columnOffset;

    if ($currentArrangement[$currentRow][$checkedCol] == "." && $currentArrangement[$currentRow][$checkedCol]) {
        checkDirection($checkedRow, $checkedCol, $currentArrangement, $columnOffset, $rowOffset);
    } else {
        print_r($currentArrangement[$checkedRow][$checkedCol]);
        return $currentArrangement[$checkedRow][$checkedCol];
    }
}

// findFirstSeatsInSight(0, 0, $testCase);

checkDirection(0, 0, $testCase, 0, 1);
