const inputValidation = (state = "", action) => {
  switch (action.type) {
    case "SEND_VALUE":
      return action.payload;
    default:
      return state;
  }
};

export default inputValidation;
