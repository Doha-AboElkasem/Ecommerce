import React from 'react';
import bgImage from '../assets/bg-plants.png'; 

const Hero = () => {
  return (
    <div
      // 1. استخدمنا relative عشان يحجز مكانه وما يخليش السكاشن اللي بعده تطلع فوقه
      // 2. h-screen بتضمن إن السكشن واخد طول الشاشة بالكامل
      className="relative h-screen w-full flex items-center justify-center text-white bg-cover bg-no-repeat overflow-hidden"
      style={{
        backgroundImage: `linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)), url(${bgImage})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        // السطر ده بيخلي الصورة ثابتة وأنت بتعمل Scroll (تأثير احترافي)
        backgroundAttachment: 'fixed', 
      }}
    >
      <div className="text-center px-4 z-10">
        {/* نصوص الهيرو */}
        <p className="text-sm md:text-base tracking-[0.3em] uppercase mb-4 opacity-80 mt-10">
          Welcome to Urban Jungle Co.
        </p>
        
        <h1 className="text-5xl md:text-8xl font-bold leading-tight drop-shadow-2xl">
          Discover the Beauty of <span className="text-[#98bc3c]">Nature</span>
        </h1>
        
        <p className="text-lg md:text-xl mt-4 max-w-2xl mx-auto opacity-90 font-light">
          Bring life to your space with our curated collection of indoor plants.
        </p>

        {/* زرار الـ Shop Now المعدل */}
        <button className="mt-10 bg-gradient-to-r from-[#98bc3c] to-[#86a634] hover:from-[#86a634] hover:to-[#759028] text-white font-bold px-16 py-5 rounded-full text-xl shadow-2xl hover:shadow-3xl transition-all duration-300 hover:scale-110 hover:-translate-y-1 border-2 border-transparent hover:border-white/20 uppercase tracking-widest">
          Shop Now
        </button>
      </div>

      {/* سهم لتحت عشان المستخدم يعرف إن فيه محتوى تحت */}
      <div className="absolute bottom-10 left-1/2 transform -translate-x-1/2 animate-bounce opacity-50">
        <svg xmlns="http://www.w3.org/2000/svg" className="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M19 14l-7 7m0 0l-7-7m7 7V3" />
        </svg>
      </div>
    </div>
  );
};

export default Hero;