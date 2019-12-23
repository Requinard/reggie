import React from 'react'
import {Divider, Paper, Typography, withStyles} from '@material-ui/core'
import LoginForm from "./LoginForm";
import {connect} from 'react-redux';
import PropTypes from 'prop-types';
import {login} from '../../../actions/login'

const styles = theme => ({
  main: {
    width: 'auto',
    display: 'block', // Fix IE 11 issue.
    marginLeft: theme.spacing.unit * 3,
    marginRight: theme.spacing.unit * 3,
    [theme.breakpoints.up(400 + theme.spacing.unit * 3 * 2)]: {
      width: 400,
      marginLeft: 'auto',
      marginRight: 'auto',
    },
  },
  paper: {
    marginTop: theme.spacing.unit * 8,
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    padding: `${theme.spacing.unit * 2}px ${theme.spacing.unit * 3}px ${theme.spacing.unit * 3}px`,
  },
});

class LoginComponent extends React.Component {
  constructor(props) {
    super(props);

    this.register = () => {
      this.props.history.push('/auth/register/')
    }
  }

  handleSubmit = (values) => this.props.login(values)
    .then(() => console.log("yes"))
    .catch(() => console.error("no"))

  render() {
    const {classes} = this.props;
    return (
      <div className={classes.main}>
        <Paper className={classes.paper}>
          <Typography variant="h4">
            Welcome to Reggie
          </Typography>
          <Divider/>
          <LoginForm onSubmit={this.handleSubmit} register={this.register}/>
        </Paper>
      </div>
    )
  }
}

LoginComponent.propTypes = {
  login: PropTypes.func.isRequired,
  isLoggedIn: PropTypes.bool
};

function mapStateToProps(state) {
  return {
    isLoggedIn: state.login.isLoggedIn
  }
}

function mapDispatchToProps(dispatch) {
  return {
    login: values => {
      dispatch(login(values))
    }
  }
}

const ReduxLoginComponent = connect(
  mapStateToProps,
  mapDispatchToProps
)(LoginComponent)

export default withStyles(styles)(ReduxLoginComponent)
