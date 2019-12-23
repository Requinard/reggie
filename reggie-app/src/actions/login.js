import {LOGIN_FAILEd, LOGIN_PENDING, LOGIN_SUCCEEDED} from '../reducers/login'

import ReggieApi from '../api/ReggieApi'

export function login(values) {
  return (dispatch) => {
    dispatch({type: LOGIN_PENDING, username: values['username']})

    ReggieApi.postAuthJwtCreate(values.username, values.password)
      .then(response => dispatch({type: LOGIN_SUCCEEDED, data: response.body}))
      .catch(error => dispatch({type: LOGIN_FAILEd, error}))
  }
}
