import React from 'react';

const ProductCard = ({ title, price, image }) => {
  return (
    <article className="bg-white rounded-2xl shadow-lg overflow-hidden hover:shadow-2xl transition-shadow">
      <div className="w-full h-64 bg-gray-100">
        <img src={image} alt={title} className="w-full h-full object-cover" />
      </div>
      <div className="p-5">
        <h3 className="text-lg font-semibold text-gray-900 mb-2">{title}</h3>
        <div className="flex items-center justify-between">
          <span className="text-2xl font-extrabold text-gray-900">${price}</span>
          <button className="inline-flex items-center gap-2 bg-[#98bc3c] hover:bg-[#86a634] text-white px-4 py-2 rounded-full text-sm transition">
            Add
          </button>
        </div>
      </div>
    </article>
  );
};

export default ProductCard;
