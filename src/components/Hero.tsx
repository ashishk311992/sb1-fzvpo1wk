import React from 'react';
import { Shield, Truck, BadgeCheck } from 'lucide-react';

export function Hero() {
  return (
    <div className="relative bg-blue-700">
      <div className="absolute inset-0">
        <img
          className="w-full h-full object-cover mix-blend-multiply filter brightness-50"
          src="https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?auto=format&fit=crop&q=80"
          alt="Commercial vehicles on highway"
        />
      </div>
      
      <div className="relative max-w-7xl mx-auto py-24 px-4 sm:py-32 sm:px-6 lg:px-8">
        <h1 className="text-4xl font-extrabold tracking-tight text-white sm:text-5xl lg:text-6xl">
          Simplifying Vehicle Compliance
        </h1>
        <p className="mt-6 text-xl text-gray-100 max-w-3xl">
          Get AIS 140 certification and the best insurance quotes for your commercial vehicles. 
          Trust our expertise to keep your fleet compliant and protected.
        </p>
        <div className="mt-10">
          <a
            href="#interest-form"
            className="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-blue-700 bg-white hover:bg-gray-50 shadow-lg"
          >
            Get Started
          </a>
        </div>
      </div>
    </div>
  );
}