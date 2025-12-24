export default function TopBar() {
  return (
    <header className="w-full h-full px-12 flex items-center justify-between glass-header pointer-events-auto">
      <div>
        <h1 className="text-xl font-medium">Assistant IA</h1>
        <p className="text-sm text-glass">Analyse & génération locale</p>
      </div>
      <span className="text-sm text-glass">Modèle : Qwen</span>
    </header>
  );
}
