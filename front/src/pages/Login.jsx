import {useState} from "react";
import {Link} from "react-router-dom";

export default function Login() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault();

        if (!email || !password) {
            setError("Veuillez remplir tous les champs.");
            return;
        }

        // Simuler une validation simple
        if (email !== "test@example.com" || password !== "password") {
            setError("Identifiants incorrects.");
            return;
        }

        setError("");
        alert("Connexion réussie !");
    };

    return (
        <div className="flex min-h-screen items-center justify-center dark:bg-gray-900">
            <div className="w-full max-w-md bg-white dark:bg-gray-800 p-8 rounded-xl">
                <h2 className="text-2xl font-bold text-center text-gray-800 dark:text-white">RentalAi</h2>

                {error && (
                    <div className="mt-4 p-2 text-sm text-red-700 bg-red-200 rounded-md">
                        {error}
                    </div>
                )}

                <form onSubmit={handleSubmit} className="mt-6 flex flex-col gap-2">
                    <div>
                        <label className="block text-gray-700 dark:text-gray-300">Email</label>
                        <input
                            type="email"
                            className="block w-full max-h-48 p-3 text-gray-900 border border-gray-300 rounded-2xl bg-gray-50 text-base focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 resize-none pr-10"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                        />
                    </div>

                    <div>
                        <label className="block text-gray-700 dark:text-gray-300">Mot de passe</label>
                        <input
                            type="password"
                            className="block w-full max-h-48 p-3 text-gray-900 border border-gray-300 rounded-2xl bg-gray-50 text-base focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 resize-none pr-10"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                        />
                    </div>

                    <button
                        type="submit"
                        className="w-full mt-6 bg-blue-500 hover:bg-blue-700 text-white p-3 rounded-2xl transition"
                    >
                        Se connecter
                    </button>
                </form>

                <p className="mt-4 text-sm text-center text-gray-600 dark:text-gray-300">
                    Pas encore de compte ? <Link to="/register" className="text-blue-500">Inscrivez-vous</Link>
                </p>
            </div>
        </div>
    );
}