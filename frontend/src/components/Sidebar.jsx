import { LayoutDashboard, Cpu, Boxes } from "lucide-react"

export default function Sidebar() {
  return (
    <aside
      className="
        w-64
        bg-card/40
        backdrop-blur-md
        border-r border-white/10
        p-4
      "
    >
      <nav className="flex flex-col gap-1">
        <SidebarItem icon={<LayoutDashboard size={18} />} label="Dashboard" />
        <SidebarItem icon={<Boxes size={18} />} label="Models" />
        <SidebarItem icon={<Cpu size={18} />} label="System" />
      </nav>
    </aside>
  )
}

function SidebarItem({ icon, label }) {
  return (
    <button
      className="
        flex items-center gap-3
        px-3 py-2
        rounded-lg
        text-sm
        text-white/70
        hover:text-white
        hover:bg-white/10
        transition
      "
    >
      {icon}
      {label}
    </button>
  )
}
