import {useContext} from "react";
import {Navigate, Outlet} from "react-router-dom";

const PrivateRoutes = () => {
    const user = true
    return user ? <Outlet/> : <Navigate to="/login"/>;
};

export default PrivateRoutes;