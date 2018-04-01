// node_module imports
import React from 'react';
import ReactDOM from 'react-dom';

// app module imports
import NoteCard from './components/Notecard/index';

const styles = {
  app: {
    paddingTop: 40,
    textAlign: 'center',
  },
};

class App extends React.Component {
  constructor() {
    super();

    this.state = {
      word: 'abstemious',
      definition: 'restraint especially in the consumption of food or alcohol',
      classification: 'adjective'
    }
  }
  
  render() {
    return (
      <div style={styles.app}>
        <p>Welcome to Word Stock! Hope you learn something new!</p>
        <NoteCard word={this.state.word} definition={this.state.definition}
          classification={this.state.classification} />
      </div>
    );
  }
};

const root = document.querySelector('#app');
ReactDOM.render(<App />, root);
