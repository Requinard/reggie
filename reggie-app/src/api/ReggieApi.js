import axios from 'axios';

class ReggieApi {
  constructor(){
    this.URL = 'localhost:8000/api/'
  }

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
    console.log("Logging in", username, password);
    console.log(this.URL + 'auth/jwt/create')
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
