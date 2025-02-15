import React from "react";

const Footer = () => {
  return (
    <footer className="w-full bg-gray-800 p-4 mt-10 text-center text-white">
      <p>&copy; {new Date().getFullYear()} Resume Matcher. All rights reserved.</p>
    </footer>
  );
};

export default Footer;
