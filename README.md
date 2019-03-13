# Reggie

A new regserver for events with the goal of being crash and DDoS resillient.

## Goals

- Seperate front and back
- Run the frontend on a seperate, load balanced server
- Use backend only for responding to requests
- Use proper rate-limiting
- Allow for an extended registration process


# Components

Reggie is made out of the following components

## reggie-server

A python & django based backend server.

## reggie-app

A react JS web app that is used to complete the registration process

## reggie-hammer

A solution to benchmark the server.
