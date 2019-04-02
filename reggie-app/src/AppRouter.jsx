import React from 'react';
import {HashRouter as Router, Route, Switch} from 'react-router-dom';
import Auth from "./components/auth/Auth";

let AppRouter = () => (
  <Router>
    <Switch>
      <Route to="/auth/" component={Auth}/>
      <Route component={Auth}/>
    </Switch>
  </Router>
);


export default AppRouter;
