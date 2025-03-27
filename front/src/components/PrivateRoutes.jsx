import {useContext} from "react";
import {Navigate, Outlet} from "react-router-dom";

const PrivateRoutes = () => {
    const user
    return user ? <Outlet/> : <Navigate to="/login"/>;
};

export default PrivateRoutes;