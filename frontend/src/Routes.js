import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import GlobalStyles from 'src/GlobalStyles';
import SellerAccountManagement from 'src/pages/SellerAccountManagement';
import SideBar from 'src/component/sideBar/SideBar';

// const store = createStore(rootReducer);

const Routes = () => {
  return (
    <Router>
      <GlobalStyles />
      <Switch>
        <Route exact path="/" component={SideBar} />
        <Route exact path="/seller" component={SellerAccountManagement} />
      </Switch>
    </Router>
  );
};
export default Routes;
