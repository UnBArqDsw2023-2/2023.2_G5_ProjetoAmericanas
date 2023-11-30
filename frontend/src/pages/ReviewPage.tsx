import React from 'react';
import { useState,  } from 'react';
import Rating from '@mui/material/Rating';
import { useParams } from 'react-router-dom';
import allProducts from '../assets/all_products';
import './ReviewPage.css';
import { Link } from 'react-router-dom';

const ReviewPage: React.FC = () => {
  const { productId } = useParams<{ productId: string }>();
  const product = allProducts.find(item => item.id.toString() === productId);
  const [value, setValue] = useState("");
  const [value1, setValue1] = useState("");
  const [value2, setValue2] = useState("");
  const [value3, setValue3] = useState("");

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
          <div className='ratting'>
            <Rating
              name="simple-controlled"
              value ={value}
              onChange={(event, newValue) => {
                setValue(newValue);
              }}
            />
          </div>
          <h3>custo-benefício</h3>
          <div className='ratting'>
            <Rating
              name="simple-controlled"
              value ={value1}
              onChange={(event, newValue) => {
                setValue1(newValue);
              }}
            />
          </div>
          <h3>qualidade</h3>
          <div className='ratting'>
            <Rating
              name="simple-controlled"
              value ={value2}
              onChange={(event, newValue) => {
                setValue2(newValue);
              }}
            />
          </div>
          <h3>tamanho</h3>
          <div className='ratting'>
            <Rating
              name="simple-controlled"
              value ={value3}
              onChange={(event, newValue) => {
                setValue3(newValue);
              }}
            />
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
