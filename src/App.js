import './App.css';
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import TrendingProducts from "./components/TrendingProducts";

function App() {
  return (
   
    <div className="w-full min-h-screen overflow-x-hidden">
      <Navbar />
      <Hero />
      <TrendingProducts />
     
    </div>
  );
}
export default App;
