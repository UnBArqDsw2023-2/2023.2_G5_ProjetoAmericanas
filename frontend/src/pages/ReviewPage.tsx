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
    <div className='review-main'>
      <div className="review-page-container">
        <h1>Avalie o Produto</h1>
        <div className='review-first'>
          <div className='review-title'>
            <img className='product-image' src={product.image} alt={product.name} />
            <span>{product.name}</span>
          </div>
          <h3>o que você achou do produto?</h3>
          <div class="rate">
            <input type="radio" id="star5" name="rate" value="5" />
            <label for="star5" title="text">5 stars</label>
            <input type="radio" id="star4" name="rate" value="4" />
            <label for="star4" title="text">4 stars</label>
            <input type="radio" id="star3" name="rate" value="3" />
            <label for="star3" title="text">3 stars</label>
            <input type="radio" id="star2" name="rate" value="2" />
            <label for="star2" title="text">2 stars</label>
            <input type="radio" id="star1" name="rate" value="1" />
            <label for="star1" title="text">1 star</label>
          </div>
          <h3>custo-benefício</h3>
          <div class="rate">
            <input type="radio" id="star5" name="rate" value="5" />
            <label for="star5" title="text">5 stars</label>
            <input type="radio" id="star4" name="rate" value="4" />
            <label for="star4" title="text">4 stars</label>
            <input type="radio" id="star3" name="rate" value="3" />
            <label for="star3" title="text">3 stars</label>
            <input type="radio" id="star2" name="rate" value="2" />
            <label for="star2" title="text">2 stars</label>
            <input type="radio" id="star1" name="rate" value="1" />
            <label for="star1" title="text">1 star</label>
          </div>
          <h3>qualidade</h3>
          <div class="rate">
            <input type="radio" id="star5" name="rate" value="5" />
            <label for="star5" title="text">5 stars</label>
            <input type="radio" id="star4" name="rate" value="4" />
            <label for="star4" title="text">4 stars</label>
            <input type="radio" id="star3" name="rate" value="3" />
            <label for="star3" title="text">3 stars</label>
            <input type="radio" id="star2" name="rate" value="2" />
            <label for="star2" title="text">2 stars</label>
            <input type="radio" id="star1" name="rate" value="1" />
            <label for="star1" title="text">1 star</label>
          </div>
          <h3>tamanho</h3>
          <div class="rate">
            <input type="radio" id="star5" name="rate" value="5" />
            <label for="star5" title="text">5 stars</label>
            <input type="radio" id="star4" name="rate" value="4" />
            <label for="star4" title="text">4 stars</label>
            <input type="radio" id="star3" name="rate" value="3" />
            <label for="star3" title="text">3 stars</label>
            <input type="radio" id="star2" name="rate" value="2" />
            <label for="star2" title="text">2 stars</label>
            <input type="radio" id="star1" name="rate" value="1" />
            <label for="star1" title="text">1 star</label>
          </div>
        </div>
        <div className="review-form">
          <h3>escreva sua avaliação</h3>
          <input type="text" id="title" name="title" placeholder='título da avaliação'/>
          <br />
          <textarea id="comment" name="comment" placeholder='avaliação do produto' />
        </div>
        < Link to="/reviewdone">
          <button>Enviar Avaliação</button>
        </ Link>
      </div>
    </div>
  );
};

export default ReviewPage;
