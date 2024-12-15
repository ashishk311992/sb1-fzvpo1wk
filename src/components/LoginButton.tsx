import React from 'react';
import { LogIn, LogOut, User } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import { useNavigate } from 'react-router-dom';

export function LoginButton() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  if (user) {
    return (
      <div className="flex items-center space-x-4">
        <div className="flex items-center text-gray-700">
          <User className="h-5 w-5 mr-2" />
          <span>{user.name}</span>
        </div>
        <button
          onClick={logout}
          className="flex items-center px-4 py-2 text-sm font-medium text-gray-700 hover:text-blue-600"
        >
          <LogOut className="h-5 w-5 mr-2" />
          Logout
        </button>
      </div>
    );
  }

  return (
    <button
      onClick={() => navigate('/login')}
      className="flex items-center px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-md hover:bg-blue-700"
    >
      <LogIn className="h-5 w-5 mr-2" />
      Login
    </button>
  );
}