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

$keys = array();
$data = prepData();
$count = 0;

class Bag {
    public function __construct($bag_name, $contained_bags)
    {
        $this->bag_name = $bag_name;
        $this->contained_bags = $contained_bags;
    }

    public function getBagName()
    {
        return $this->bag_name;
    }

    public function getContainedBags($data)
    {
        return array_filter($data, function ($obj) {
            if (in_array($obj->bag_name, $this->contained_bags)) {
                return true;
            }
        }
        );
        // return $this->contained_bags;
    }

    public function hasGoldBag()
    {
        $searchTerm = "shiny gold bags";
        if (in_array($searchTerm, $this->contained_bags)) {
            return true;
        } else {
            return false;
        }
    }

    public function containsNoBags()
    {
        $searchTerm = "no other bags";
        if (in_array($searchTerm, $this->contained_bags)) {
            return true;
        } else {
            return false;
        }
    }
}

 /**
  * Prepares dataset to be used

  * @return object
  */
function prepData()
{
    $response = array();
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

        $addedBag = new Bag($key, $rules);

        array_push($response, $addedBag);
    }

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

    return trim($formattedBag);
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
    // print_r($data);
    $count = 0;


    foreach ($data as $bag) {
        if (checkForGoldBag($bag, $data)) {
            $count++;
        }
    }

    echo $count;

}

function checkForGoldBag($bag, $data)
{
    if ($bag->hasGoldBag()) {
        return true;
    } else if ($bag->containsNoBags()) {
        return false;
    } else {
        foreach ($bag->getContainedBags($data) as $bagToCheck) {
            if (checkForGoldBag($bagToCheck, $data)) {
                return true;
            };
        }
    }
}

checkBags($data, $count);
echo($count);