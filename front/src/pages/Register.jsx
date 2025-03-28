import {useFormik} from "formik";
import * as Yup from "yup";
import {Link, useNavigate} from "react-router-dom";
import {register} from "../api/auth.js";

export default function Register() {
    const navigate = useNavigate();

    const validationSchema = Yup.object({
        name: Yup.string()
            .required("Veuillez entrer votre nom."),
        email: Yup.string()
            .email("Adresse email invalide.")
            .required("Veuillez remplir l'email."),
        password: Yup.string()
            .min(6, "Le mot de passe doit contenir au moins 6 caractères.")
            .required("Veuillez remplir le mot de passe."),
    });

    const formik = useFormik({
        initialValues: {
            name: "",
            email: "",
            password: "",
        },
        validationSchema,
        onSubmit: async (values) => {
            try {
                const response = await register(values.name, values.email, values.password);

                if (response) {
                    navigate("/login");
                } else {
                    alert(response.message || "Une erreur est survenue.");
                }
            } catch (error) {
                alert("Une erreur est survenue lors de l'inscription.");
            }
        }
    });

    return (
        <div className="flex min-h-screen items-center justify-center">
            <div className="w-full max-w-md bg-white p-8 rounded-xl">
                <h2 className="text-2xl font-bold text-center text-gray-800">RentalAi</h2>

                <form onSubmit={formik.handleSubmit} className="mt-6 flex flex-col gap-2">
                    <div>
                        <label className="block text-gray-700">Nom</label>
                        <input
                            type="text"
                            name="name"
                            className="block w-full p-3 text-gray-900 border border-gray-300 rounded-2xl bg-gray-50 text-base focus:ring-blue-500 focus:border-blue-500"
                            value={formik.values.name}
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur}
                        />
                        {formik.touched.name && formik.errors.name && (
                            <div className="text-red-600 text-sm">{formik.errors.name}</div>
                        )}
                    </div>

                    <div>
                        <label className="block text-gray-700">Email</label>
                        <input
                            type="email"
                            name="email"
                            className="block w-full p-3 text-gray-900 border border-gray-300 rounded-2xl bg-gray-50 text-base focus:ring-blue-500 focus:border-blue-500"
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
                            className="block w-full p-3 text-gray-900 border border-gray-300 rounded-2xl bg-gray-50 text-base focus:ring-blue-500 focus:border-blue-500"
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
                        S'inscrire
                    </button>
                </form>

                <p className="mt-4 text-sm text-center text-gray-600">
                    Déjà un compte ? <Link to="/login" className="text-blue-500">Connectez-vous</Link>
                </p>
            </div>
        </div>
    );
}