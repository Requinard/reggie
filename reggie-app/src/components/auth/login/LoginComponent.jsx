import React from 'react'
import {withStyles, Paper, Typography} from '@material-ui/core'
import LoginForm from "./LoginForm";

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
})

class LoginComponent extends React.Component {
  constructor(props) {
    super(props);

    this.onSubmit = (values) => {
      console.log(values);
    };

    this.register = () => {
      this.props.history.push('/auth/register/')
    }
  }
  render() {
    const { classes } = this.props;
    return (
      <div className={classes.main}>
        <Paper className={classes.paper}>
          <Typography variant="h4">
            Welcome to Reggie
          </Typography>
          <LoginForm onSubmit={this.onSubmit} register={this.register} />
        </Paper>
      </div>
    )
  }
}

export default withStyles(styles)(LoginComponent)
