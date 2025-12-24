import Sidebar from "./Sidebar";
import TopBar from "./TopBar";
import AIChatPanel from "./AIChatPanel";

export default function MainPanel() {
  return (
    <div className="flex h-screen w-screen overflow-hidden">
      
      <Sidebar />

      <div className="flex-1 flex flex-col">
        <TopBar />
        <AIChatPanel />
      </div>

    </div>
  );
}
