import React from 'react';
import { Shield, Truck, BadgeCheck, Clock, IndianRupee, HeartHandshake } from 'lucide-react';

export function Features() {
  const features = [
    {
      icon: <Shield className="h-8 w-8 text-blue-600" />,
      title: 'AIS 140 Certification',
      description: 'Complete certification assistance with expert guidance throughout the process'
    },
    {
      icon: <IndianRupee className="h-8 w-8 text-blue-600" />,
      title: 'Lowest Insurance Quotes',
      description: 'Compare and get the best insurance rates from top providers'
    },
    {
      icon: <Clock className="h-8 w-8 text-blue-600" />,
      title: 'Quick Processing',
      description: 'Fast-track your applications with our efficient processing system'
    },
    {
      icon: <HeartHandshake className="h-8 w-8 text-blue-600" />,
      title: 'Dedicated Support',
      description: '24/7 assistance from our experienced team of professionals'
    }
  ];

  return (
    <div className="bg-gray-50 py-16">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center">
          <h2 className="text-3xl font-extrabold text-gray-900 sm:text-4xl">
            Why Choose Us
          </h2>
          <p className="mt-4 text-lg text-gray-600">
            We make commercial vehicle compliance simple, fast, and hassle-free
          </p>
        </div>

        <div className="mt-20 grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-4">
          {features.map((feature, index) => (
            <div key={index} className="bg-white rounded-lg shadow-lg p-6 text-center">
              <div className="flex justify-center">{feature.icon}</div>
              <h3 className="mt-4 text-lg font-medium text-gray-900">{feature.title}</h3>
              <p className="mt-2 text-gray-600">{feature.description}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}