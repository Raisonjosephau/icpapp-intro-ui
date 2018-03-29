import { BottomNavigation } from 'react-native-material-ui';
import React, { Component } from 'react';
import {NavigationActions} from 'react-navigation';
import { Alert } from 'react-native'
import PropTypes from 'prop-types';

const propTypes = {
    navigation: PropTypes.shape({
        goBack: PropTypes.func.isRequired,
    }).isRequired,
};



class TabNav extends Component {
    
    constructor() {
        super();
        this.state = {
          active: 'Page1',
        };
        //this.renderSelectedTab();
    }
    navigateToScreen = (route) => () => {
        this.setState({active: route});
        this.props.navigation.navigate(route)
    }

    showAlert = () => {
        Alert.alert(
           'You need to...'
        )

    }

    render() {
        return (
            <BottomNavigation active={this.state.active}>
                <BottomNavigation.Action
                    key="Page1"
                    icon="today"
                    label="Login"   
                    onPress={() =>  this.setState({active: 'Page2'})}
                />
                <BottomNavigation.Action
                    key="Page2"
                    icon="people"
                    label="Signup"
                    onPress={() =>  this.props.navigation.navigate('Page2')}
                />
            </BottomNavigation>
        )
    }
  }


  TabNav.propTypes = propTypes;
  export default TabNav;