import TopBar from "../components/TopBar"
import Sidebar from "../components/Sidebar"

export default function AppLayout({ children }) {
  return (
    <div className="w-screen h-screen bg-black text-white overflow-hidden">
      <TopBar />

      <div className="flex h-[calc(100vh-3.5rem)]">
        <Sidebar />

        <main className="flex-1 p-6 overflow-y-auto">
          {children}
        </main>
      </div>
    </div>
  )
}
