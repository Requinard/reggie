import React from 'react'
import {Route, Switch} from 'react-router-dom'
import LoginComponent from "./login/LoginComponent";

let Auth = () => (
  <Switch>
    <Route component={LoginComponent}/>
  </Switch>
)

export default Auth
