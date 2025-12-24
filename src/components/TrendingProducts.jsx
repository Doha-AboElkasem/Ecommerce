import React from 'react';
import ProductCard from './ProductCard';


const TrendingProducts = () => {
  // داتا المنتجات حطيتها هنا عشان السيكشن يكون مسؤول عن بياناته
  const products = [
    {
      id: 1,
      title: "Starlight Succulent",
      price: "95",
      image: "https://images.unsplash.com/photo-1509423350716-97f9360b4e5f?q=80&w=500&auto=format&fit=crop"
    },
    {
      id: 2,
      title: "Silver Mist",
      price: "92",
      image: "https://images.unsplash.com/photo-1545241047-6083a3684587?q=80&w=500&auto=format&fit=crop"
    },
    {
      id: 3,
      title: "Golden Glow",
      price: "85",
      image: "https://images.unsplash.com/photo-1501004318641-729e8e26bd05?q=80&w=500&auto=format&fit=crop"
    }
  ];

  return (
    <section className="py-24 px-4 md:px-10 max-w-7xl mx-auto bg-white">
      {/* العنوان بروح التصميم اللي بعته */}
      <div className="text-center mb-20">
        <h2 className="text-4xl font-light tracking-tight text-gray-900 mb-4">Trending Products</h2>
        <div className="w-12 h-[2px] bg-[#98bc3c] mx-auto"></div>
      </div>
      
      {/* شبكة المنتجات */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-x-8 gap-y-16">
        {products.map((product) => (
          <ProductCard 
            key={product.id}
            title={product.title}
            price={product.price}
            image={product.image}
          />
        ))}
      </div>
    </section>
  );
};

export default TrendingProducts;
