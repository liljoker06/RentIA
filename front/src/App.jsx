import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register.jsx";
import PrivateRoutes from "./components/PrivateRoutes.jsx";

function App() {
    return (
        <Router>
            <Routes>
                {/* Page protégée */}
                <Route element={<PrivateRoutes />}>
                    <Route path="/home" element={<Home />} />
                </Route>

                {/* Routes publiques */}
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />

                {/* Redirection automatique de / vers /login */}
                <Route path="/" element={<Navigate to="/login" />} />
            </Routes>
        </Router>
    );
}

export default App;
