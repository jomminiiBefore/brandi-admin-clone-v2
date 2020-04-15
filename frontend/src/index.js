import React from 'react';
import ReactDOM from 'react-dom';
import { createStore } from 'redux';
import { Provider } from 'react-redux';
import rootReducer from 'src/store/reducers';
import Routes from 'src/Routes';
// index.js import 설정

const wrapper = document.getElementById('container');
const store = createStore(
  rootReducer,
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
);

wrapper
  ? ReactDOM.render(
      <Provider store={store}>
        <Routes />,
      </Provider>,
      wrapper
    )
  : false;
