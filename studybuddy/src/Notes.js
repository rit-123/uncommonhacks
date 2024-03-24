import * as React from 'react';
import './Notes.css';

function Notes(props) {
  return (
    <div className="Notes">
        <div className="notesWindow">
          {props.text}
          <button className="quizButton">Practice Questions!</button>
        </div>
    </div>
  );
}

export default Notes;