import React from "react";
import { Link } from "react-router-dom";
import { Menu, MenuOption } from "./style";

function Header() {
  const options = [
    {
      label: "Previsão",
      route: "/",
    },
    {
      label: "Dashboard",
      route: "/dashboard",
    },
  ];

  return (
    <Menu>
      {options.map((item, index) => (
        <Link to={item.route}>
          <MenuOption>{item.label}</MenuOption>
        </Link>
      ))}
    </Menu>
  );
}

export default Header;
