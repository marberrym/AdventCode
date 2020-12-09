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
$partOneSolution = solvePartOne($data);
$partTwoSolution = solvePartTwo($data, $partOneSolution);

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

/**
 * Part 1 of the algorithm
 *
 * @param array $data The data to use for the algorithm
 *
 * @return int
 */
function solvePartOne($data)
{
    $preambleSize = 25;
    $invalidNumbers = array();

    for ($x=0; $x<count($data); $x++) {
        if ($x>($preambleSize - 1)) {
            $targetSum = $data[$x];
            $rangeMin = $x - $preambleSize;
            $isNumberValid = false;

            $testNumbers = array_slice($data, $rangeMin, $preambleSize);

            foreach ($testNumbers as $value1) {
                foreach ($testNumbers as $value2) {
                    if (($value1 + $value2) == $data[$x]) {
                        $isNumberValid = true;
                    }
                }
            }

            if (!$isNumberValid) {
                array_push($invalidNumbers, $targetSum);
                return $data[$x];
            }
        }
    }
}

/**
 * Part 2 of the algorithm
 *
 * @param array $data      The dataset used in part one
 * @param int   $targetSum The result from part one solution
 *
 * @return int
 */
function solvePartTwo($data, $targetSum)
{
    $startIndex = 0;
    $endIndex = 0;

    $currentSum = array_values($data)[0];

    while ($startIndex < count($data)) {
        if ($currentSum == $targetSum) {
            $contiguousSums = array_slice(
                $data,
                $startIndex,
                ($endIndex - $startIndex)
            );

            $solution = min($contiguousSums) + max($contiguousSums);
            return $solution;
        } elseif ($currentSum < $targetSum) {
            $endIndex++;
            $currentSum += array_values($data)[$endIndex];
        } else {
            $currentSum -= array_values($data)[$startIndex];
            $startIndex++;
        }
    }
}

print_r("Part One Solution: {$partOneSolution} \n");
print_r("Part Two Solution: {$partTwoSolution} \n");

?>