import React from 'react'
import {Field, reduxForm} from 'redux-form'
import {Checkbox, TextField} from 'redux-form-material-ui'
import {Button} from '@material-ui/core'

const LoginForm = (props) => {
  const handleSubmit = props;
  return (
    <form onSubmit={handleSubmit} fullWidth>
      <div>
        <Field name="username" component={TextField} type="text" label="username"/>
      </div>
      <div>
        <Field name="password" component={TextField} type="password" label="Password"/>
      </div>
      <div>
        <Field name="remember" component={Checkbox} defaultChecked={true} label="Remember me?"/>
      </div>
      <div>
        <Field type="tet"/>
      </div>
      <br/>
      <div>
        <Button variant="contained" color="secondary"
                onClick={props.register}>Register</Button>
        <Button variant="contained" color="primary" onClick={props.handleSubmit}>Login</Button>
      </div>
    </form>
  )
};

const ReduxLoginForm = reduxForm({
  form: 'login'
})(LoginForm)

export default ReduxLoginForm;
