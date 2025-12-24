import { useState } from "react";
import Sidebar from "./components/Sidebar";
import TopBar from "./components/TopBar";
import Dashboard from "./pages/Dashboard";

function App() {
  const [activeTab, setActiveTab] = useState("chat");

  return (
    <div className="w-full h-full flex liquid-metal-bg relative">
      
      {/* SIDEBAR */}
      <Sidebar activeTab={activeTab} setActiveTab={setActiveTab} />

      {/* MAIN */}
      <div className="flex-1 flex flex-col relative z-10">
        
        {/* TOPBAR */}
        <div className="h-24 relative z-20 pointer-events-auto">
          <TopBar activeTab={activeTab} />
        </div>

        {/* CONTENT */}
        <div className="flex-1 relative z-10 overflow-hidden">
          <Dashboard />
        </div>

      </div>
    </div>
  );
}

export default App;
