export const sendValue = value => {
  console.log("value:", value);
  return {
    type: "SEND_VALUE",
    value: value
  };
};
