import { BrowserRouter, Routes, Route } from "react-router-dom";
import Login from "@/components/Authentication/Login/Login";
import Signup from "@/components/Authentication/Signup/Signup";
import Landing from "@/components/Users/Navbar/Landing";
import UserProfile from "@/pages/Users/UserProfile";
import UploadPresentation from "@/pages/Users/UploadPresentation";
import GalleryCard from "@/components/GalleryCard";
import GuestGallery from "@/components/Guest/Gallery/GuestGallery";
import About from "@/components/About/About";
import Comment from "@/components/Users/Comment/Comment";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<GuestGallery />} />
        <Route path="/login/" element={<Login />} />
        <Route path="/signup/" element={<Signup />} />
        <Route path="/about/" element={<About />} />
        <Route path="/landing/" element={<Landing />} />
        <Route path="/card/" element={<GalleryCard />} />
        <Route path="/profile/" element={<UserProfile />} />
        <Route path="/upload/" element={<UploadPresentation />} />
        <Route path="/comment-section/" element={<Comment />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
