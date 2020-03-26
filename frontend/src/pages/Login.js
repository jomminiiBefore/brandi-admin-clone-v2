import React from "react";
import img from "./animation.png";
import styled from "styled-components";

const Login = () => {
  console.log("img:: ", img);
  return (
    <div>
      Login page12313123
      <BGImage />
    </div>
  );
};

export default Login;

const BGImage = styled.div`
  background-image: url("https://cdn.pixabay.com/photo/2018/03/02/09/44/butterfly-3192737_1280.png");
  width: 600px;
  height: 600px;
`;
