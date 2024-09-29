import styled from "styled-components";

export const Menu = styled.nav`
  width: 100%;
  height: 50px;
  display: flex;
  justify-content: space-between;

  a {
    text-decoration: none;
    width: 50%;
    color: #000;
  }
`;

export const MenuOption = styled.div`
  padding: 20px 0;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.3rem;

  &:hover {
    background-color: aliceblue;
  }
`;
