import React, { useState } from "react";
import ReactDOM from "react-dom";
import Routes from "src/Routes";

const wrapper = document.getElementById("container");
wrapper ? ReactDOM.render(<Routes />, wrapper) : false;
