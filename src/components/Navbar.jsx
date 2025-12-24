import React from 'react';
// 1. هنعمل import لنفس الصورة بنفس المسار
import bgImage from '../assets/bg-plants.png'; 

const Navbar = () => {
  return (
    <nav
      className="navbar fixed top-0 left-0 w-full z-[100] px-6 py-4 shadow-lg transition-all duration-300"
      style={{
        // 2. هنضيف نفس الـ style اللي في الهيرو عشان الصورة تكمل بعضها
        backgroundImage: `linear-gradient(rgba(0,0,0,0.35), rgba(0,0,0,0.35)), url(${bgImage})`,
        backgroundSize: 'cover',
        backgroundRepeat: 'no-repeat',
        backgroundPosition: 'top center', // مهم جداً عشان الصورة تبدأ من فوق
      }}
    >
      <div className="flex-1">
        <a className="text-2xl font-black text-white tracking-tighter cursor-pointer drop-shadow-md">
          URBAN <span className="text-[#98bc3c]">JUNGLE</span>
        </a>
      </div>

      <div className="flex-none hidden md:flex items-center gap-10 mr-10 text-white font-semibold">
        <a className="hover:text-[#98bc3c] transition-colors cursor-pointer">Home</a>
        <a className="hover:text-[#98bc3c] transition-colors cursor-pointer">Shop</a>
        <a className="hover:text-[#98bc3c] transition-colors cursor-pointer">About</a>
        <a className="hover:text-[#98bc3c] transition-colors cursor-pointer">Contact</a>
      </div>

      <div className="flex-none flex items-center gap-4">
        <div className="indicator text-white">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z" />
          </svg>
          <span className="badge badge-sm indicator-item bg-[#98bc3c] border-none text-black font-bold">2</span>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;