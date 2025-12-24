export default function Sidebar({ activeTab, setActiveTab }) {
  const item = (tab) =>
    `w-12 h-12 flex items-center justify-center rounded-xl cursor-pointer
     ${activeTab === tab ? "bg-white text-black" : "text-neutral-500 hover:bg-neutral-900"}
     transition-all`;

  return (
    <aside className="relative z-30 w-20 h-full glass-panel flex flex-col items-center py-8 gap-6">
      <button onClick={() => setActiveTab("chat")} className={item("chat")}>💬</button>
      <button onClick={() => setActiveTab("dashboard")} className={item("dashboard")}>📊</button>
      <button onClick={() => setActiveTab("system")} className={item("system")}>⚙️</button>
    </aside>
  );
}
