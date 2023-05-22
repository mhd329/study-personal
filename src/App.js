import { BrowserRouter, Routes, Route } from 'react-router-dom';
import ConfirmButton from './components/ConfirmButton';
import LandingPage from './components/LandingPage';
import AttendanceBook from './components/AttendanceBook';
import Reservation from './components/Reservation';
import SignUp from './components/SignUp';
import Calculator from './components/calculator/Calculator';
import './App.css';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<App />} />
          <Route path="/button" element={<ConfirmButton />} />
          <Route path="/landing-page" element={<LandingPage />} />
          <Route path="/attendance" element={<AttendanceBook />} />
          <Route path="/reservation" element={<Reservation />} />
          <Route path="/signup" element={<SignUp />} />
          <Route path="/calculator" element={<Calculator />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
