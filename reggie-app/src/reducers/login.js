export const LOGIN_SUCCEEDED = 'LOGIN_SUCCEEDED'
export const LOGIN_FAILEd = 'LOGIN_FAILED'
export const LOGIN_PENDING = 'LOGIN_PENDING'

export function login(state = {
  isLoggedIn: false
}, action) {
  switch (action.type) {
    default:
      return state;
  }
}
