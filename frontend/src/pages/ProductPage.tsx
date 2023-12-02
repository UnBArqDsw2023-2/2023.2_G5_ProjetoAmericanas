
import React from 'react';
import { useParams, Link } from 'react-router-dom';
import allProducts from '../assets/all_products';
import './ProductPage.css';

interface Review {
  title: string;
  comment: string;
}

const ProductPage: React.FC= () => {
  const { productId } = useParams<{ productId: string }>();
  const product = allProducts.find(item => item.id.toString() === productId);


  if (!product) {
    return <div>Produto não encontrado.</div>;
  }

  return (
    <div className="product-page-container">
      <div className="product-details">
        <h2>{product.name}</h2>
        <img src={product.image} alt={product.name} />
        <p>{`Preço: $${product.new_price.toFixed(2)}`}</p>
        <Link to={`/product/${product.id}/review`} className="review-button">
          Avaliar Produto
        </Link>
        <div>
          <h3>Avaliações</h3>

        </div>
      </div>
    </div>
  );
};

export default ProductPage;
