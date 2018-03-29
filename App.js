import React, { Component } from 'react';
import Router from './Tabnav/NavTab';

import { COLOR, ThemeProvider } from 'react-native-material-ui';

// you can set your style right here, it'll be propagated to application
const uiTheme = {
    palette: {
        primaryColor: COLOR.green800,
    },
    toolbar: {
        container: {
            height: 50,
        },
    },
};


export default class App extends Component {
    render() {
        return ( 
            <ThemeProvider uiTheme = { uiTheme } >
                <Router/>
            </ThemeProvider>
        );
    }
}