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
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3,
);

sort($testCase);

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

    sort($split);

    print_r($split);

    return $split;
}

function solvePartOne($data)
{
    $adaptChangeByOne = 1;
    $adaptChangeByThree = 1;

    for ($x = 0; $x < count($data); $x++) {

        print_r("Checking {$data[$x]}\n");
        print_r("Next adapter {$data[$x+1]}\n");
        if ($data[$x + 1]) {
            if (($data[$x + 1] - $data[$x]) == 3) {
                $adaptChangeByThree++;
                print_r("Change by three {$adaptChangeByThree}\n");
            } elseif (($data[$x + 1] - $data[$x]) == 1) {
                $adaptChangeByOne++;
                print_r("Change by one {$adaptChangeByOne}\n");
            }
        }
    }

    print_r("Change by one {$adaptChangeByOne}\n");
    print_r("Change by three {$adaptChangeByThree}\n");

    return $adaptChangeByOne * $adaptChangeByThree;
}

print_r($patOneSolution);