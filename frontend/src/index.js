import React from 'react';
import ReactDOM from 'react-dom';
// import { createStore } from 'redux';
import { Provider } from 'react-redux';
// import rootReducer from 'src/store/RootReducer';
import Routes from 'src/Routes';

const wrapper = document.getElementById('container');
// const store = createStore(rootReducer);

wrapper
  ? ReactDOM.render(
      // <Provider store={store}>
      <Routes />,
      // </Provider>,
      wrapper
    )
  : false;
