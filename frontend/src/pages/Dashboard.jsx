export default function Dashboard() {
  return (
    <div className="grid grid-cols-3 gap-6">
      <StatCard title="CPU Usage" />
      <StatCard title="GPU Usage" />
      <StatCard title="RAM Usage" />
    </div>
  )
}

function StatCard({ title }) {
  return (
    <div className="
      bg-card/60
      backdrop-blur-md
      border border-white/10
      rounded-xl
      p-4
    ">
      <h3 className="text-sm text-white/70 mb-2">{title}</h3>
      <div className="text-2xl font-bold">--%</div>
    </div>
  )
}
