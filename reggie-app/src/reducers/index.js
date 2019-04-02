import {login} from './login'
import { reducer as formReducer } from 'redux-form'
import {combineReducers} from 'redux'

const reducers = combineReducers({
  login,
  form: formReducer
});

export default reducers;
