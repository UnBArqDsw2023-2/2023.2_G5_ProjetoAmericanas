import React from 'react';
import { useParams } from 'react-router-dom';
import allProducts from '../assets/all_products';
import './ReviewPage.css';
import { Link } from 'react-router-dom';

const ReviewPage: React.FC = () => {
  const { productId } = useParams<{ productId: string }>();
  const product = allProducts.find(item => item.id.toString() === productId);

  if (!product) {
    return <div>Produto não encontrado.</div>;
  }

  return (
    <div className="review-page-container">
      <h2>Avaliar Produto</h2>
      <div className="review-form">
        <img src={product.image} alt={product.name} />
        <h3>{product.name}</h3>
        <label htmlFor="title">Título:</label>
        <input type="text" id="title" name="title" />
        <br />
        <label htmlFor="comment">Comentário:</label>
        <textarea id="comment" name="comment" />
        <br />
        < Link to="/reviewdone">
          <button>Enviar Avaliação</button>
        </ Link>
      </div>
    </div>
  );
};

export default ReviewPage;
