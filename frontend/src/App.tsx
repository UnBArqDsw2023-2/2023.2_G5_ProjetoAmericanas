import { memo } from 'react';
import type { FC } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { Navbar } from './component/Navbar/Navbar.js';
import ProductList from './pages/ProductList';
import ProductPage from './pages/ProductPage';
import ReviewPage from './pages/ReviewPage';
import ReviewSuccess from './pages/ReviewSuccess.js';


interface Props {
  className?: string;
}
export const App: FC<Props> = memo(function App(props = {}) {

  return (
    <Router>
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<ProductList />} />
        <Route path="/product/:productId" element={<ProductPage />} />
        <Route path="/product/:productId/review" element={<ReviewPage />} />
        <Route  path="/reviewdone" element={<ReviewSuccess/>}/>
      </Routes>
    </div>
  </Router>
  );
});
