import { BrowserRouter, Routes, Route } from 'react-router-dom';
import ConfirmButton from './components/ConfirmButton';
import LandingPage from './components/LandingPage';
import './App.css';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<App />} />
          <Route path="/button" element={<ConfirmButton />} />
          <Route path="/landing-page" element={<LandingPage />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
