import {LOGIN_FAILEd, LOGIN_PENDING, LOGIN_SUCCEEDED} from '../reducers/login'

import ReggieApi from '../api/ReggieApi'

export function login(username, password) {
  return (dispatch) => {
    dispatch({type: LOGIN_PENDING, username})

    ReggieApi.postAuthJwtCreate(username, password)
      .then(response => dispatch({type: LOGIN_SUCCEEDED, data: response.body}))
      .catch(error => dispatch({type: LOGIN_FAILEd, error}))
  }
}
