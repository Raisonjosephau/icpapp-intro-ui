/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 * @flow
 */

import PropTypes from 'prop-types';
import React, {Component} from 'react';
import {NavigationActions} from 'react-navigation';
import {ScrollView, Text, View, StyleSheet} from 'react-native';

import { Avatar, Drawer, Toolbar } from 'react-native-material-ui';


var styles = StyleSheet.create({
    items: {
      fontSize: 40
    }
  });


const propTypes = {
    navigation: PropTypes.shape({
        goBack: PropTypes.func.isRequired,
    }).isRequired,

      style: PropTypes.shape({
        item: View.propTypes.style,
        icon: styles.items,
        value: styles.items,
        label: styles.items
    }),
};



class SideMenu extends Component {

    constructor() {
        super();
        this.state = {
          active: 'Page1'
        };
        //this.renderSelectedTab();
      }
  navigateToScreen = (route) => () => {

    this.setState({active: route});

    const navigateAction = NavigationActions.navigate({
      routeName: route
    });
    this.props.navigation.dispatch(navigateAction);
  }

  render () {
    return (
      <View style={{flex: 1, elevation: 4, backgroundColor: 'white' }}>
              <Drawer>
                        <Drawer.Header >
                            <Drawer.Header.Account
                                avatar={<Avatar text="A" />}
                                footer={{
                                    dense: true,
                                    centerElement: {
                                        primaryText: 'Reservio',
                                        secondaryText: 'business@email.com',
                                    },
                                    rightElement: <Text>js</Text>,
                                }}
                            />
                        </Drawer.Header>
                        <Drawer.Section  style={{value:{fontSize:20}}}
                            divider
                            items={[
                                {  icon: 'bookmark-border', value: 'Page1', active: this.state.active==='Page1',onPress: this.navigateToScreen('Page1') },
                                { icon: 'today', value: 'Page2', active: this.state.active==='Page2', onPress: this.navigateToScreen('Page2') },
                                { icon: 'people', value: 'Page3', active: this.state.active==='Page3',onPress: this.navigateToScreen('Page3') },
                            ]}
                        />
                        <Drawer.Section
                            title="Personal"
                            items={[
                                { icon: 'info', value: 'Info' },
                                { icon: 'settings', value: 'Settings' },
                            ]}
                        />
                    </Drawer>
      </View>
    );
  }
}

SideMenu.propTypes = propTypes;
export default SideMenu;