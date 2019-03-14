import React, {Component} from 'react';
import './App.css';
import {createStore} from 'redux';
import {Provider} from 'react-redux';
import reducers from './reducers/index';
import Overview from "./components/overview";

const store = createStore(reducers);

class App extends Component {
  render() {
    return (
      <div className="App">
        <Provider store={store}>
          <Overview/>
        </Provider>
      </div>
    );
  }
}

export default App;
