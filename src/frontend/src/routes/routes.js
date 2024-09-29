import { createBrowserRouter } from "react-router-dom";
import Homepage from "../pages/home";
import DogecoinGraph from "../pages/dashboard";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <Homepage />,
  },
  {
    path: "/dashboard",
    element: <DogecoinGraph />,
  },
]);
