import React from 'react';
import './ReviewSuccess.css';

const ReviewSuccess: React.FC = () => {
  return (
    <div className="review-success-container">
      <h2 className="review-success-title">Sua avaliação foi enviada :)</h2>
      <p className="review-success-text">Ela vai ser analisada e em breve publicada na página do produto, tá?</p>
    </div>
  );
};

export default ReviewSuccess;
