import { useState, useRef } from 'react';
import { ArrowRight } from "lucide-react";
import { askRenalIA } from "../api/renalIA";
import ReactMarkdown from "react-markdown";
import { logout } from "../api/auth";
import ConfirmationModal from "../components/ConfirmationModal";

function Home() {
  const [value, setValue] = useState('');
  const [messages, setMessages] = useState([]);
  const [isConfirming, setIsConfirming] = useState(false); // État pour contrôler l'affichage du modal
  const textareaRef = useRef(null);

  const handleInputChange = (e) => {
    const newValue = e.target.value;
    setValue(newValue);

    if (textareaRef.current) {
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
      const response = await askRenalIA(userMessage, "");
      setMessages((prev) => [...prev, { from: "bot", text: response }]);
    } catch (err) {
      setMessages((prev) => [...prev, { from: "bot", text: "❌ Erreur de réponse de l'IA." }]);
    }
  };

  const handleLogout = () => {
    setIsConfirming(true); // Ouvre la fenêtre de confirmation
  };

  const handleConfirmLogout = () => {
    logout(); // Déconnecter l'utilisateur
    setIsConfirming(false); // Fermer le modal après confirmation
  };

  const handleCloseModal = () => {
    setIsConfirming(false); // Fermer le modal sans déconnexion
  };

  return (
    <>
      {/* Modal de confirmation */}
      <ConfirmationModal
        isOpen={isConfirming}
        onClose={handleCloseModal}
        onConfirm={handleConfirmLogout}
      />

      {/* Bouton logout fixe en haut à gauche */}
      <button
        onClick={handleLogout}
        className="fixed top-4 left-4 text-sm text-red-500 border border-red-500 px-3 py-1 rounded-lg hover:bg-red-500 hover:text-white transition z-50"
      >
        Se déconnecter
      </button>

      <div className="flex items-center justify-center h-screen">
        <div
          className={`mb-6 w-full max-w-xl flex flex-col gap-2 h-full ${messages.length === 0 ? 'flex-1 justify-center' : ''}`}>
          <div
            className={`mt-2 pt-4 space-y-2 flex flex-col items-end ${messages.length > 0 ? 'flex-1 overflow-y-auto' : ''}`}>
            {messages.map((message, index) => (
              <div
                key={index}
                className={`p-2 rounded-xl inline-block max-w-full ${message.from === "user" ? "bg-blue-100 self-end" : "bg-gray-200 self-start"}`}
                style={{
                  wordWrap: "break-word",
                  maxWidth: "calc(100% - 30px)"
                }}
              >
                <ReactMarkdown>{message.text}</ReactMarkdown>
              </div>
            ))}
          </div>

          {!messages.length && (
            <h2 className="block mb-2 text-2xl font-medium text-gray-900 text-center">
              Bienvenue sur RentalAI, comment puis-je vous aider?
            </h2>
          )}

          <div className="relative">
            <textarea
              id="large-textarea"
              value={value}
              onChange={handleInputChange}
              ref={textareaRef}
              rows="1"
              className="block w-full max-h-48 p-4 text-gray-900 border border-gray-300 rounded-2xl bg-gray-50 text-base focus:ring-blue-500 focus:border-blue-500 resize-none pr-10"
            />
            <button
              onClick={handleSend}
              className="absolute right-2 top-1/2 transform -translate-y-1/2 bg-blue-500 text-white border border-blue-500 rounded-xl p-1 hover:bg-blue-700 hover:border-blue-700 focus:outline-none"
            >
              <ArrowRight color="white" />
            </button>
          </div>
        </div>
      </div>
    </>
  );
}

export default Home;
