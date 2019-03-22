import React, {Component} from 'react';
import './App.css';
import {createStore, applyMiddleware} from 'redux';
import {Provider} from 'react-redux';
import reducers from './reducers/index';
import Overview from "./components/overview";
import thunk from 'redux-thunk';

const store = createStore(
  reducers,
  applyMiddleware(thunk)
);

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
