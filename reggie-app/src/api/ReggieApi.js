import axios from 'axios';

class ReggieApi {
  constructor(){
    this.URL = 'localhost:8000/api/'
  }

  getConventions() {
    return axios.get(this.getUrl() + 'conventions')
  }

  postAuthUserRegister(username, password, email) {
    return axios.post(
      this.getUrl() + 'auth/users/create',
      {
        username,
        password,
        email
      }
    )
  }

  postAuthJwtCreate(username, password) {
    return axios.post(
      this.getUrl() + 'auth/jwt/create',
      {
        username,
        password
      }
    )
  }
}

const instance = new ReggieApi();

export default instance;
