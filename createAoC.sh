#!/bin/bash

while getopts y:d:l: flag
do
    case "${flag}" in
        y) year=${OPTARG};;
        d) day=${OPTARG};;
        l) language=${OPTARG};;
    esac
done

YEAR_ROOT="$HOME/Documents/codeSpace/adventCode/$year"
DAY_ROOT="$HOME/Documents/codeSpace/adventCode/$year/day$day"

create_php_file () {
    touch "$DAY_ROOT/day$day.php"
    echo "<?php" >> "$DAY_ROOT/day$day.php"
    echo "" >> "$DAY_ROOT/day$day.php"
    echo "\$file=\"input.txt\";" >> "$ROOT/day$day.php"
    echo "\$fopen = fopen(\$file, \"read\");" >> "$DAY_ROOT/day$day.php"
    echo "\$fread = fread(\$fopen, filesize(\$file));" >> "$DAY_ROOT/day$day.php"
    echo "fclose(\$fopen);" >> "$DAY_ROOT/day$day.php"
    echo "\$input=explode(\"\n\", \$fread);" >> "$DAY_ROOT/day$day.php"
    echo "" >> "$DAY_ROOT/day$day.php"
    echo "\$tfile=\"testCase.txt\";" >> "$DAY_ROOT/day$day.php"
    echo "\$tfopen = fopen(\$tfile, \"read\");" >> "$DAY_ROOT/day$day.php"
    echo "\$tfread = fread(\$tfopen, filesize(\$tfile));" >> "$DAY_ROOT/day$day.php"
    echo "fclose(\$tfopen);" >> "$DAY_ROOT/day$day.php"
    echo "\$test=explode(\"\n\", \$tfread);" >> "$DAY_ROOT/day$day.php"
    echo "" >> "$DAY_ROOT/day$day.php"
    echo "function main(\$data)" >> "$DAY_ROOT/day$day.php"
    echo "{" >> "$DAY_ROOT/day$day.php"
    echo "" >> "$DAY_ROOT/day$day.php"
    echo "}" >> "$DAY_ROOT/day$day.php"
    echo "" >> "$DAY_ROOT/day$day.php"
    echo "main(\$test);" >> "$DAY_ROOT/day$day.php"
    echo "Created PHP file"
}

create_python_file () {
    touch "$DAY_ROOT/day$day.py"
    echo "f = open('input.txt', 'r');" >> "$DAY_ROOT/day$day.py"
    echo "input = f.read().splitlines();" >> "$DAY_ROOT/day$day.py"
    echo "tf = open('testCase.txt', 'r');" >> "$DAY_ROOT/day$day.py"
    echo "test = tf.read().splitlines();" >> "$DAY_ROOT/day$day.py"
    echo "" >> "$DAY_ROOT/day$day.py"
    echo "def main(input):" >> "$DAY_ROOT/day$day.py"
    echo "" >> "$DAY_ROOT/day$day.py"
    echo "main(test)" >> "$DAY_ROOT/day$day.py"
    echo "Created python file"
}

create_node_file () {
    touch "$DAY_ROOT/day$day.js"
    echo "const fs = require('fs');" >> "$DAY_ROOT/day$day.js"
    echo "let input = fs.readFileSync('input.txt', 'utf8').split('\n');" >> "$DAY_ROOT/day$day.js"
    echo "let test = fs.readFileSync('testCase.txt', 'utf8').split('\n');" >> "$DAY_ROOT/day$day.js"
    echo "" >> "$DAY_ROOT/day$day.js"
    echo "const main = (input) => {" >> "$DAY_ROOT/day$day.js"
    echo "" >> "$DAY_ROOT/day$day.js"
    echo "}" >> "$DAY_ROOT/day$day.js"
    echo "" >> "$DAY_ROOT/day$day.js"
    echo "main(test);" >> "$DAY_ROOT/day$day.js"
    echo "Created node file"

}

create_file () {
    case $language in
        "php" | "PHP")
            create_php_file
            ;;
        "python" | "py")
            create_python_file
            ;;
        "node" | "js")
            create_node_file
            ;;
        *)
            echo "Unknown language"
            ;;
    esac
}

if [ -d "$YEAR_ROOT" ]
then
    if [ -d "$DAY_ROOT" ]
    then
        echo "Day $day already exists"
    else
        mkdir "$DAY_ROOT"
        touch "$DAY_ROOT/input.txt"
        touch "$DAY_ROOT/testCase.txt"
        create_file
        echo "Created $year Day $day"
    fi
else
    mkdir "$YEAR_ROOT"
    mkdir "$DAY_ROOT"
    touch "$DAY_ROOT/input.txt"
    touch "$DAY_ROOT/testCase.txt"
    create_file
    echo "created new AoC year $year with a directory for day $day"
fi

