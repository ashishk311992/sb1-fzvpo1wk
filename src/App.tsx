import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Toaster } from 'react-hot-toast';
import { AuthProvider } from './contexts/AuthContext';
import { Header } from './components/Header';
import { Hero } from './components/Hero';
import { Features } from './components/Features';
import { InterestForm } from './components/InterestForm';
import { Footer } from './components/Footer';
import { LoginPage } from './pages/LoginPage';

export function App() {
  return (
    <Router>
      <AuthProvider>
        <div className="min-h-screen bg-gray-50">
          <Toaster position="top-right" />
          <Routes>
            <Route
              path="/"
              element={
                <>
                  <Header />
                  <main>
                    <Hero />
                    <Features />
                    <InterestForm />
                  </main>
                  <Footer />
                </>
              }
            />
            <Route path="/login" element={<LoginPage />} />
          </Routes>
        </div>
      </AuthProvider>
    </Router>
  );
}