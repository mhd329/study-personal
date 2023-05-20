import { BrowserRouter, Routes, Route } from 'react-router-dom';
import ConfirmButton from './components/ConfirmButton';
import './App.css';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<App />} />
          <Route path="/button" element={<ConfirmButton />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
