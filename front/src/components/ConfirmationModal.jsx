import React from "react";

const ConfirmationModal = ({ isOpen, onClose, onConfirm }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 flex justify-center items-center bg-gray-600 bg-opacity-50 z-50">
      <div className="bg-white p-6 rounded-lg shadow-lg w-96">
        <h3 className="text-xl font-semibold text-gray-800">Confirmer la déconnexion</h3>
        <p className="mt-2 text-gray-600">Êtes-vous sûr de vouloir vous déconnecter ?</p>
        <div className="mt-4 flex justify-end gap-4">
          <button
            onClick={onClose}
            className="bg-gray-300 text-gray-700 px-4 py-2 rounded-md hover:bg-gray-400"
          >
            Annuler
          </button>
          <button
            onClick={onConfirm}
            className="bg-red-500 text-white px-4 py-2 rounded-md hover:bg-red-600"
          >
            Confirmer
          </button>
        </div>
      </div>
    </div>
  );
};

export default ConfirmationModal;
