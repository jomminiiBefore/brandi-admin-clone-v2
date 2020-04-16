import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import GlobalStyles from 'src/GlobalStyles';
import SideBar from 'src/component/sideBar/SideBar';
import Login from 'src/pages/Login';
import SignUp from 'src/pages/SignUp';
import SellerAccountManagement from 'src/pages/SellerAccountManagement';
import SellerInfoEdit from 'src/pages/SellerInfoEdit';
import LoginOk from 'src/pages/LoginOk';
import ProductRegist from 'src/pages/ProductRegist';
import ColorFilter from 'src/component/productRegist/ColorFilter';
import SellerSelect from 'src/component/productRegist/SellerSelect';
import ProductModify from 'src/pages/ProductModify';
import ProductManagement from 'src/pages/ProductManagement';

const Routes = () => {
  return (
    <Router>
      <GlobalStyles />
      <Switch>
        <Route exact path="/" component={Login} />
        <Route exact path="/login" component={Login} />
        <Route exact path="/signup" component={SignUp} />
        <Route exact path="/loginOk" component={LoginOk} />
        <Route exact path="/seller" component={SellerAccountManagement} />
        <Route exact path="/sellerInfoEdit" component={SellerInfoEdit} />
        <Route exact path="/product" component={ProductManagement} />
        <Route exact path="/productRegist" component={ProductRegist} />
        <Route exact path="/colorFilter" component={ColorFilter} />
        <Route exact path="/sellerSelect" component={SellerSelect} />
        <Route exact path="/productModify" component={ProductModify} />
      </Switch>
    </Router>
  );
};
export default Routes;
