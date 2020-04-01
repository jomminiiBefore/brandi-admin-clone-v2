import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import GlobalStyles from "src/GlobalStyles";
import SellerAccountManagement from "src/pages/SellerAccountManagement";
import SideBar from "src/component/sideBar/SideBar";
import Login from "src/pages/Login";
import SignUp from "src/pages/SignUp";

const Routes = () => {
  return (
    <Router>
      <GlobalStyles />
      <Switch>
        <Route exact path="/" component={SideBar} />
        <Route exact path="/seller" component={SellerAccountManagement} />
        <Route exact path="/signup" component={SignUp} />
      </Switch>
    </Router>
  );
};
export default Routes;
