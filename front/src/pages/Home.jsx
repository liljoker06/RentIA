import { useState, useRef } from 'react';
import { ArrowRight, SendIcon } from "lucide-react";
import { askRenalIA } from "../api/renalIA";
import ReactMarkdown from "react-markdown";

function Home() {
    const [value, setValue] = useState('');
    const [messages, setMessages] = useState([]); // Etat pour stocker les messages envoyés
    const textareaRef = useRef(null);

    const handleInputChange = (e) => {
        const newValue = e.target.value;
        setValue(newValue);

        // Ajuster la hauteur du textarea pour correspondre au contenu
        if (textareaRef.current) {
            // Réinitialise la hauteur pour ajuster dynamiquement
            textareaRef.current.style.height = 'auto';
            textareaRef.current.style.height = `${textareaRef.current.scrollHeight}px`;
        }
    };

    const handleSend = async () => {
        if (value.trim() === "") return;

        const userMessage = value;
        setMessages((prev) => [...prev, { from: "user", text: userMessage }]);
        setValue("");

        try {
            const response = await askRenalIA(userMessage, ""); // ou récupère le vrai nom s’il est stocké
            setMessages((prev) => [...prev, { from: "bot", text: response }]);
        } catch (err) {
            setMessages((prev) => [...prev, { from: "bot", text: "❌ Erreur de réponse de l'IA." }]);
        }
    };

    return (
        <div className="flex items-center justify-center h-screen">
            <div
                className={`mb-6 w-full max-w-xl flex flex-col gap-2 h-full ${messages.length === 0 ? 'flex-1 justify-center' : ''}`}>
                {/* Afficher les messages envoyés */}
                <div
                    className={`mt-2 pt-4 space-y-2 flex flex-col items-end ${messages.length > 0 ? 'flex-1 overflow-y-auto' : ''}`}>
                    {messages.map((message, index) => (
                        <div
                            key={index}
                            className={`p-2 rounded-xl inline-block max-w-full ${message.from === "user" ? "bg-blue-100 self-end" : "bg-gray-200 self-start"
                                }`}
                            style={{
                                wordWrap: "break-word",
                                maxWidth: "calc(100% - 30px)"
                            }}
                        >
                            <ReactMarkdown>{message.text}</ReactMarkdown>
                        </div>
                    ))}
                </div>

                {!messages.length &&
                    <h2
                        className="block mb-2 text-2xl font-medium text-gray-900">
                        Bienvenue sur RentalAI, comment puis-je vous aider?
                    </h2>}

                <div className="relative">
                    <textarea
                        id="large-textarea"
                        value={value}
                        onChange={handleInputChange}
                        ref={textareaRef}
                        rows="1"
                        className="block w-full max-h-48 p-4 text-gray-900 border border-gray-300 rounded-2xl bg-gray-50 text-base focus:ring-blue-500 focus:border-blue-500 resize-none pr-10"
                    />
                    {/* Bouton d'envoi */}
                    <button
                        onClick={handleSend}
                        className="absolute right-2 top-1/2 transform -translate-y-1/2 bg-blue-500 text-white border border-blue-500 rounded-xl p-1 hover:bg-blue-700 hover:border-blue-700 focus:outline-none"
                    >
                        <ArrowRight color="white" />
                    </button>
                </div>
            </div>
        </div>
    );
}

export default Home;