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
    "F10",
    "N3",
    "F7",
    "R90",
    "F11",
);

$patOneSolution = solvePartOne($data);

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
    return $split;
}

function solvePartOne($data)
{
    $currentDirection = "E";

    $latitude = 0;
    $longitude = 0;

    foreach ($data as $command) {
        $direction = substr($command, 0, 1);
        $value = substr($command, 1);

        print_r("{$direction}{$value}\n");

        if ($direction == "L" || $direction == "R") {
            $timesCalled = $value / 90;
            for($x=0; $x<$timesCalled; $x++) {
                $currentDirection = changeDirection($direction, $currentDirection);
            }
        } else {
            $newResults = moveShip($currentDirection, $direction, $value, $latitude, $longitude);
        }

        print_r($newResults);
        $latitude = $newResults->latitude;
        $longitude = $newResults->longitude;

        print_r($latitude);
        print_r("\n");
        print_r($longitude);
    }

    print_r($latitude);
    print_r($longitude);
    print_r("Latitude: {$latitude} \n Longitude {$longitude}\n");

    $manhattanDistance = abs($latitude) + abs($longitude);

    print_r("Manhattan value: {$manhattanDistance}");

    print_r(1256 + 700);

}

function moveShip($currentDirection, $newDirection, $value, $latitude, $longitude)
{
    if ($newDirection == "F") {
        return traverse($currentDirection, $value, $latitude, $longitude);
    } else {
        return traverse($newDirection, $value, $latitude, $longitude);
    }
}

function traverse($direction, $value, $latitude, $longitude) {
    switch($direction) {
    case "N":
        $latitude += $value;
        $obj = (object) array(
            "latitude" => $latitude,
            "longitude" => $longitude
        );
        return $obj;
    case "E":
        $longitude += $value;
        $obj = (object) array(
            "latitude" => $latitude,
            "longitude" => $longitude
        );
        return $obj;
    case "S":
        $latitude -= $value;
        $obj = (object) array(
            "latitude" => $latitude,
            "longitude" => $longitude
        );
        return $obj;
    case "W":
        $longitude -= $value;
        $obj = (object) array(
            "latitude" => $latitude,
            "longitude" => $longitude
        );
        return $obj;
    }
}

function changeDirection($direction, $currentDirection) {
    if ($direction == "R") {
        switch($currentDirection) {
        case "N":
            return "E";
        case "E":
            return "S";
        case "S":
            return "W";
        case "W":
            return "N";
        }
    } else if ($direction == "L") {
        switch($currentDirection) {
        case "N":
            return "W";
        case "E":
            return "N";
        case "S":
            return "E";
        case "W":
            return "S";
        }
    }
}
