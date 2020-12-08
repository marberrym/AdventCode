const fs = require('fs');

let input = fs.readFileSync('input.txt', 'utf8').split('\n\n');

const analyzeAnswers = () => {
    let groupAnswers = [];
    let totalAnswers = 0;
    input.forEach(group => {
        let questionsAnswered = [];
        let questionsAnsweredByAll;
        const persons = group.split('\n');

        persons.forEach(person => {
            [...person].forEach(answer => {
                questionsAnswered.push(answer);
            })
        });

        questionsAnsweredByAll = didAllAnswer(questionsAnswered, persons.length);

        groupAnswers.push(questionsAnsweredByAll.length);
    })

    groupAnswers.forEach(answerGroup => totalAnswers += answerGroup);
    console.log("Total answers answered by all in a group: ", totalAnswers);
}

const didAllAnswer = (answers, groupSize) => {
    let answeredByAll = [];
    answers.forEach(answer => {
        if (answers.filter(checkedAnswer => checkedAnswer === answer).length === groupSize && !answeredByAll.includes(answer)) {
            answeredByAll.push(answer);
        }
    })

    return answeredByAll;
}

analyzeAnswers();