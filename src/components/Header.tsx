import React from 'react';
import { Truck, Phone, Menu } from 'lucide-react';
import { LoginButton } from './LoginButton';

export function Header() {
  return (
    <header className="bg-white shadow-sm">
      <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16 items-center">
          <div className="flex items-center">
            <Truck className="h-8 w-8 text-blue-600" />
            <span className="ml-2 text-xl font-bold text-gray-900">VehicleComply</span>
          </div>
          
          <div className="hidden md:flex items-center space-x-8">
            <a href="/" className="text-gray-700 hover:text-blue-600">Home</a>
            <a href="/about" className="text-gray-700 hover:text-blue-600">About</a>
            <a href="/contact" className="text-gray-700 hover:text-blue-600">Contact</a>
            <a href="tel:+919876543210" className="flex items-center text-blue-600">
              <Phone className="h-5 w-5 mr-2" />
              <span>+91 98765 43210</span>
            </a>
            <LoginButton />
          </div>
          
          <div className="md:hidden">
            <button className="text-gray-700">
              <Menu className="h-6 w-6" />
            </button>
          </div>
        </div>
      </nav>
    </header>
  );
}