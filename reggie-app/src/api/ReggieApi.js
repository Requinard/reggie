import axios from 'axios';

class ReggieApi {
  URL = 'localhost:8000/api/'

  getConventions() {
    return axios.get(this.URL + 'conventions')
  }

  postAuthUserRegister(username, password, email) {
    return axios.post(
      this.URL + 'auth/users/create',
      {
        username,
        password,
        email
      }
    )
  }

  postAuthJwtCreate(username, password) {
    return axios.post(
      this.URL + 'auth/jwt/create',
      {
        username,
        password
      }
    )
  }
}

const instance = new ReggieApi();

export default instance;
