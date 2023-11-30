
import React from 'react';
import allProducts from '../assets/all_products';
import './ProductList.css';
import { Link } from 'react-router-dom';

const shuffleArray = (array: any[]) => {
  const shuffledArray = [...array];
  for (let i = shuffledArray.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffledArray[i], shuffledArray[j]] = [shuffledArray[j], shuffledArray[i]];
  }
  return shuffledArray;
};

const ProductList: React.FC = () => {
  const shuffledProducts = shuffleArray(allProducts);

  return (
    <div className="product-list-container">
    <h2>Lista de Produtos</h2>
    <div className="product-grid">
      {shuffledProducts.map(product => (
        <Link key={product.id} to={`/product/${product.id}`} className="product-item">
          <img src={product.image} alt={product.name} />
          <h3>{product.name}</h3>
          <p>{`Preço: $${product.new_price.toFixed(2)}`}</p>
        </Link>
      ))}
    </div>
  </div>
  );
};

export default ProductList;

