import Page1 from '../Drawer/Page1';
import Page2 from '../Drawer/Page2';
import TabNav from './TabNav';
import { TabNavigator } from 'react-navigation';

export default TabNavigator ({
    Page1: {
        screen: Page1
    },
    Page2: {
        screen: Page2
    }
}, {
    tabBarComponent: TabNav,
    tabBarPosition: 'bottom'
});