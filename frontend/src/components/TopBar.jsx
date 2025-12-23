export default function TopBar() {
  const minimize = () => window.electron?.minimize()
  const maximize = () => window.electron?.maximize()
  const close = () => window.electron?.close()

  return (
    <div
      className="w-full h-14 flex items-center justify-between px-6
      bg-card backdrop-blur-md border-b border-white/10
      select-none"
      style={{ WebkitAppRegion: "drag" }}
    >
      {/* Left */}
      <div className="flex items-center gap-3">
        <div className="w-2 h-2 rounded-full bg-accent animate-pulse" />
        <h1 className="text-sm font-semibold tracking-wide">
          Horizon AI
        </h1>
      </div>

      {/* Right */}
      <div
        className="flex items-center gap-3"
        style={{ WebkitAppRegion: "no-drag" }}
      >
        <button onClick={minimize} className="window-btn hover:bg-white/10" />
        <button onClick={maximize} className="window-btn hover:bg-white/10" />
        <button onClick={close} className="window-btn hover:bg-red-500/80" />
      </div>
    </div>
  )
}
