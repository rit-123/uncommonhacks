import * as React from 'react';
import './QuizItem.css';

function QuizItem(props) {


  const map = props.choices.map((choice, index) => {
    return (
      <div key={index} className="choices">
        <button id={index} className="choiceButton">{choice}</button>
      </div>
    );
  });
  return (
    <div className="QuizItem">
        <div className="question">{props.question}</div>
        <div className="choices">{map}</div>
        <div className="correctIncorrect"></div>
    </div>
  );
}
export default QuizItem;