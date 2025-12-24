import React from 'react';
import Sidebar from '../components/Sidebar';
import Dashboard from '../pages/Dashboard';
import AIChatPanel from '../components/AIChatPanel';
import TopBar from '../components/TopBar';

const AppLayout = ({ activeTab, setActiveTab }) => {
  return (
    // Flex Row : Navigation à gauche, Contenu à droite
    <div className="flex h-screen w-full">
      
      {/* --- SIDEBAR (Noir Absolu) --- */}
      <aside className="w-20 bg-black border-r border-white/[0.03] flex flex-col justify-between flex-shrink-0 z-20">
        <Sidebar activeTab={activeTab} setActiveTab={setActiveTab} />
      </aside>

      {/* --- MAIN CONTENT (Fond Noir) --- */}
      <main className="flex-1 flex flex-col relative min-w-0">
        
        {/* TOPBAR (Sticky) */}
        <div className="h-20 w-full glass-panel z-10 flex-shrink-0">
          <TopBar activeTab={activeTab} />
        </div>

        {/* CONTENT AREA (Scrollable) */}
        <div className="flex-1 overflow-hidden relative">
          <div className="h-full overflow-y-auto p-0">
            {activeTab === 'dashboard' && <Dashboard />}
            {activeTab === 'chat' && <AIChatPanel />}
          </div>
        </div>

      </main>
    </div>
  );
};

export default AppLayout;