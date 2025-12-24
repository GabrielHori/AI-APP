import { Send } from "lucide-react";

export default function AIChatPanel() {
  return (
    <div className="flex h-full liquid-metal-bg">

      {/* Zone principale */}
      <div className="flex-1 flex flex-col">

        {/* Messages */}
        <div className="flex-1 overflow-y-auto px-12 py-10 space-y-6">
          
          <div className="glass-panel rounded-xl p-4 max-w-xl">
            <p className="text-sm">
              Bonjour 👋 Comment puis-je t’aider aujourd’hui ?
            </p>
          </div>

        </div>

        {/* Input */}
        <div className="px-12 py-6 border-t border-white/[0.06]">
          <div className="flex items-center gap-4 glass-panel rounded-xl px-6 py-4">
            
            <input
              type="text"
              placeholder="Écris ta demande…"
              className="flex-1 bg-transparent outline-none text-sm text-white placeholder:text-glass"
            />

            <button className="btn-ghost p-2 rounded-lg">
              <Send size={18} />
            </button>

          </div>
        </div>

      </div>
    </div>
  );
}
