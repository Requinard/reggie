import React, {Component} from 'react';
import './App.css';
import {applyMiddleware, createStore} from 'redux';
import {Provider} from 'react-redux';
import reducers from './reducers/index';
import Overview from "./components/overview";
import thunk from 'redux-thunk';
import AppRouter from "./AppRouter";

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
          <div className="app-outer">
            <div className="app-inner">
              <AppRouter/>
            </div>
          </div>
        </Provider>
      </div>
    );
  }
}

export default App;
