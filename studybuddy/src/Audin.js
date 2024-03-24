import * as React from 'react';
import './Audin.css';
import Button from './Button';

function Audin() {
  return (
    <div className="Audin">
      <div className="dottedBorder"></div>
      <div className="dragArea">
        <p className="text">
          Click anywhere to choose a file.
        </p>
        <Button />
      </div>
    </div>
  );
}

export default Audin;