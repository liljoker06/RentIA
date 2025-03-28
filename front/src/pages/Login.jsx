import {useFormik} from "formik";
import * as Yup from "yup";
import {Link, useNavigate} from "react-router-dom";
import {login} from "../api/auth.js";

export default function Login() {
    const navigate = useNavigate();
    const validationSchema = Yup.object({
        email: Yup.string()
            .email("Adresse email invalide.")
            .required("Veuillez remplir l'email."),
        password: Yup.string()
            .required("Veuillez remplir le mot de passe."),
    });

    const formik = useFormik({
        initialValues: {
            email: "",
            password: "",
        },
        validationSchema,
        onSubmit: async (values) => {
            const response = await login(values.email, values.password);
            if (response) {
                navigate("/home");
            }
        }
    });

    return (
        <div className="flex min-h-screen items-center justify-center">
            <div className="w-full max-w-md bg-white p-8 rounded-xl">
                <h2 className="text-2xl font-bold text-center text-gray-800">RentalAi</h2>

                <form onSubmit={formik.handleSubmit} className="mt-6 flex flex-col gap-2">
                    <div>
                        <label className="block text-gray-700">Email</label>
                        <input
                            type="email"
                            name="email"
                            className="block w-full max-h-48 p-3 text-gray-900 border border-gray-300 rounded-2xl bg-gray-50 text-base focus:ring-blue-500 focus:border-blue-500 resize-none pr-10"
                            value={formik.values.email}
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur}
                        />
                        {formik.touched.email && formik.errors.email && (
                            <div className="text-red-600 text-sm">{formik.errors.email}</div>
                        )}
                    </div>

                    <div>
                        <label className="block text-gray-700">Mot de passe</label>
                        <input
                            type="password"
                            name="password"
                            className="block w-full max-h-48 p-3 text-gray-900 border border-gray-300 rounded-2xl bg-gray-50 text-base focus:ring-blue-500 focus:border-blue-500 resize-none pr-10"
                            value={formik.values.password}
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur}
                        />
                        {formik.touched.password && formik.errors.password && (
                            <div className="text-red-600 text-sm">{formik.errors.password}</div>
                        )}
                    </div>

                    <button
                        type="submit"
                        className="w-full mt-6 bg-blue-500 hover:bg-blue-700 text-white p-3 rounded-2xl transition"
                    >
                        Se connecter
                    </button>
                </form>

                <p className="mt-4 text-sm text-center text-gray-600">
                    Pas encore de compte ? <Link to="/register" className="text-blue-500">Inscrivez-vous</Link>
                </p>
            </div>
        </div>
    );
}