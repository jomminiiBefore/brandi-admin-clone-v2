import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import GlobalStyles from "src/GlobalStyles";
import Login from "src/pages/Login";
import SellerAccountManagement from "src/pages/SellerAccountManagement";

const Routes = () => {
  return (
    <Router>
      <GlobalStyles />
      <Switch>
        <Route exact path="/" component={Login} />
        <Route exact path="/seller" component={SellerAccountManagement} />
      </Switch>
    </Router>
  );
};
export default Routes;
