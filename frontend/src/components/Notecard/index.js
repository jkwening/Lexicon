import React from 'react';

const Notecard = (props) => {
  return (
    <div>
      <h1 id='word'>{props.word}</h1>
      <h4 id='classification'>{props.classification}</h4>
      <p id='definition'>{props.definition}</p>
    </div>
  )
};

export default Notecard;
