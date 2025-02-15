import React from "react";
import { Button } from "@/components/ui/button";

const Navbar = () => {
  return (
    <nav className="w-full bg-blue-600 p-4 shadow-md">
      <div className="container mx-auto flex justify-between items-center">
        <h1 className="text-white text-xl font-bold">Resume Matcher</h1>
        <Button className="bg-white text-blue-600 px-4 py-2 rounded-md shadow">
          Login
        </Button>
      </div>
    </nav>
  );
};

export default Navbar;
