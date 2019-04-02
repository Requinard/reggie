import React from 'react'
import {AppBar, Button, IconButton, Toolbar, Tooltip, Typography} from '@material-ui/core'
import MenuIcon from '@material-ui/icons/Menu';
import PropTypes from 'prop-types';
import {withStyles} from '@material-ui/core/styles';

const styles = {
  root: {
    flexGrow: 1
  },
  grow: {
    flexGrow: 1
  },
  menuButton: {
    marginLeft: -12,
    marginRight: 20
  }
};

class Overview extends React.Component {
  render() {
    const {classes} = this.props
    return (
      <AppBar position="static">
        <Toolbar>
          <IconButton className={classes.menuButton} color="inherit" aria-label="Menu">
            <MenuIcon/>
          </IconButton>
          <Tooltip title="Debug info goes here" className={classes.grow}>
            <Typography variant="h6" color="inherit">
              Reggie
            </Typography>
          </Tooltip>
          <Button color="inherit">Login</Button>
        </Toolbar>
      </AppBar>
    );
  }
}


Overview.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Overview);
