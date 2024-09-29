import React from "react";
import Header from "../../components/header";
import { LeftContainer, PageContainer, RightContainer } from "./style";

function Homepage() {
  return (
    <PageContainer>
      <Header />
      <LeftContainer />
      <RightContainer />
    </PageContainer>
  );
}

export default Homepage;
