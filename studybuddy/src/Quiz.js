import * as React from 'react';
import './Quiz.css';
import QuizItem from './QuizItem';

function Quiz(props) {

  return (
    <div className="Quiz">
        <div className="quizList">
            <QuizItem question="Helloo?" choices={["Huh","What","Who","Kwa"]}></QuizItem>
            <QuizItem question="Helloo?" choices={["Huh","What","Who","Kwa"]}></QuizItem>
            <QuizItem question="Helloo?" choices={["Huh","What","Who","Kwa"]}></QuizItem>
            <QuizItem question="Helloo?" choices={["Huh","What","Who","Kwa"]}></QuizItem>
            <QuizItem question="Helloo?" choices={["Huh","What","Who","Kwa"]}></QuizItem>
            <QuizItem question="Helloo?" choices={["Huh","What","Who","Kwa"]}></QuizItem>
        </div>
        <button className="controlButtonPrev" >Prev</button>
        <button className="controlButtonNext" >Next</button>
    </div>
  );
}
export default Quiz;