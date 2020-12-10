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

 /**
  * Prepares dataset to be used

  * @return object
  */
function prepData()
{

    $response = (object)
    $file="input.txt";
    $fopen = fopen($file, "read");
    $fread = fread($fopen, filesize($file));
    fclose($fopen);

    $splitBy = "\n";
    $split = explode($splitBy, $fread);

    foreach ($split as $bag) {
        $bagSplit = explode("contain", $bag);

        $key = trim(array_values($bagSplit)[0]);
        $inside = array_values($bagSplit)[1];

        $rules = formatBags($inside);

        $response->$key = $rules;
        // print_r("{$key}\n");
        // print_r("{$inside}\n");
    }

    print_r($response);

    return $response;
}

/**
 * Formats bags inside of a bag
 *
 * @param $bags string of bags contained
 *
 * @return array
 */
function formatBags($bags)
{
    // $bags = array(
    //     "2 posh purple bags",
    //     "1 muted chartreuse bag",
    //     "1 drab violet bag",
    //     "1 wavy blue bag."
    // );

    $bagsArray = explode(",", $bags);
    $formattedBags = array_map('formatBag', $bagsArray);

    return $formattedBags;

    // array_map


}

/**
 * Formats bags inside of a bag
 *
 * @param $string string of bags contained
 *
 * @return string
 */
function formatBag($string)
{
    $patternArray = array('/(\d+)/', '/(\.)/');
    $formattedBag = preg_replace($patternArray, "", $string);

    if (substr($formattedBag, -1) === "g") {
        $formattedBag = "{$formattedBag}s";
    }

    return $formattedBag;
}


/**
 * Checks bags for a gold bag
 *
 * @param $data string of bags contained
 *
 * @return string
 */
function checkBags($data)
{
    print_r(gettype($data));
    for ($x=0; $x<count($data); $x++) {
        print_r($x);
        print_r($data[$x]);
    }
    // foreach ($data as $bag) {
    //     print_r("Bag entry...");
    //     print_r($bag);
    // }
}

checkBags($data);