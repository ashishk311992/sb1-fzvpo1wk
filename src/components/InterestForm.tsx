import React, { useState } from 'react';
import { Send } from 'lucide-react';
import { createLead } from '../api/leads';
import toast from 'react-hot-toast';

export function InterestForm() {
  const [formData, setFormData] = useState({
    name: '',
    mobile: '',
    email: '',
    vehicleType: '',
    state: '',
    serviceType: '',
    comments: ''
  });

  const [isSubmitting, setIsSubmitting] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);

    try {
      await createLead(formData);
      toast.success('Thank you for your interest! We will contact you soon.');
      setFormData({
        name: '',
        mobile: '',
        email: '',
        vehicleType: '',
        state: '',
        serviceType: '',
        comments: ''
      });
    } catch (error) {
      toast.error('Failed to submit form. Please try again.');
    } finally {
      setIsSubmitting(false);
    }
  };

  // Rest of the component remains the same, just update the button to show loading state:
  return (
    <div id="interest-form" className="bg-white py-16">
      {/* Previous JSX remains the same until the submit button */}
      <button
        type="submit"
        disabled={isSubmitting}
        className="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50"
      >
        <Send className="h-5 w-5 mr-2" />
        {isSubmitting ? 'Submitting...' : 'Submit Interest'}
      </button>
    </div>
  );
}