import TopBar from "./layouts/TopBar"
import AppLayout from "./layout/AppLayout"
import Dashboard from "./pages/Dashboard"

export default function App() {
  return (
    <div className="h-screen w-screen flex flex-col">
      <TopBar />
      <main className="flex-1 p-6">
        <h2 className="text-white/60 text-sm">
          Dashboard
        </h2>
      </main>
    </div>
  )
}

export default function App() {
  return (
    <AppLayout>
      <Dashboard />
    </AppLayout>
  )
}
