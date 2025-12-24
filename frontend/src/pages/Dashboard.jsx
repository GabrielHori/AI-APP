import React, { useState, useEffect, useRef } from 'react';
import { Send, Plus, Trash2 } from 'lucide-react';

const API_URL = "http://localhost:11451/api/v1"; // Assure-toi que le backend tourne

const AIChatPanel = () => {
  // --- États ---
  const [conversations, setConversations] = useState([]);
  const [activeChatId, setActiveChatId] = useState(null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [availableModels, setAvailableModels] = useState([]);
  const [selectedModel, setSelectedModel] = useState('Qwen2.5-7b'); 

  const messagesEndRef = useRef(null);

  // --- Logique (Simulée pour le design, à remplacer par tes fetch) ---
  useEffect(() => {
    const mockData = [
      { id: '1', title: 'Architecture du projet', model: 'Qwen2.5-7b', updated_at: new Date().toISOString() },
      { id: '2', title: 'Optimisation GPU', model: 'Llama3-70b', updated_at: new Date().toISOString() }
    ];
    setConversations(mockData);
    if (mockData.length > 0) {
      setActiveChatId(mockData[0].id);
      setMessages([
        { role: 'assistant', content: 'Bienvenue. Comment puis-je vous aider ?' }
      ]);
    }
    setAvailableModels(['Qwen2.5-7b', 'Llama3-70b']);
  }, []);

  const handleSend = () => {
    if (!input.trim()) return;
    const userMsg = { role: 'user', content: input };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setIsLoading(true);
    setTimeout(() => {
      const aiMsg = { role: 'assistant', content: `Réponse simulée pour : "${input}"` };
      setMessages(prev => [...prev, aiMsg]);
      setIsLoading(false);
    }, 1000);
  };

  // --- UI Helpers ---
  const scrollToBottom = () => { messagesEndRef.current?.scrollIntoView({ behavior: "smooth" }); };
  useEffect(() => { scrollToBottom(); }, [messages]);

  const createNewChat = () => {
    setActiveChatId(null);
    setMessages([]);
    setInput('');
  };

  return (
    
    <div className="flex h-full bg-black text-white">
      <button
        onClick={() => {
          console.log("CLICK OK");
          alert("CLICK OK");
      }}
    className="fixed top-40 left-40 z-[9999] bg-red-600 text-white px-6 py-3 rounded-xl">
    TEST CLIC
      </button>

      
      {/* --- SIDEBAR DISCUSSIONS (Liste) --- */}
      <div className="w-72 bg-[#050505] border-r border-white/[0.03] flex flex-col flex-shrink-0 z-10">
        <div className="p-4 border-b border-white/[0.03]">
          <button onClick={createNewChat} className="w-full py-3 bg-white text-black font-medium rounded-xl hover:scale-[1.02] transition-transform duration-200 shadow-[0_0_20px_rgba(255,255,255,0.2)] flex items-center justify-center gap-2">
            <Plus size={20} strokeWidth={2} />
            <span>Nouvelle</span>
          </button>
        </div>

        <div className="flex-1 overflow-y-auto py-2 space-y-1">
          {conversations.map(chat => (
            <div
              key={chat.id}
              className={`mx-2 group flex items-center p-3 rounded-xl cursor-pointer transition-all duration-200 select-none border border-transparent hover:bg-white/[0.03] ${
                activeChatId === chat.id 
                  ? 'bg-white text-black border-white shadow-[0_4px_20px_rgba(255,255,255,0.1)]' 
                  : 'text-neutral-400'
              }`}
            >
              <div className="flex-1 min-w-0">
                <div className="font-medium text-sm truncate">{chat.title}</div>
                <div className="text-xs opacity-60 truncate">{chat.model}</div>
              </div>
              {/* Bouton Supprimer (Visible au survol) */}
              <button className="opacity-0 group-hover:opacity-100 text-black/50 hover:text-red-500 ml-2 transition-opacity">
                <Trash2 size={16} strokeWidth={1.5} />
              </button>
            </div>
          ))}
        </div>
      </div>

      {/* --- ZONE PRINCIPALE (Chat) --- */}
      <div className="flex-1 flex flex-col bg-[#000000] relative">
        
        {/* Header (Modèle + Titre) */}
        <div className="h-20 border-b border-white/[0.03] flex items-center justify-between px-12">
          <div className="flex items-center gap-3">
            <h2 className="text-lg font-medium text-white tracking-wide">
              {activeChatId ? conversations.find(c => c.id === activeChatId)?.title : "Nouvelle Discussion"}
            </h2>
          </div>

          {/* Selecteur de Modèle Minimaliste */}
          <select 
            value={selectedModel} 
            onChange={(e) => setSelectedModel(e.target.value)}
            disabled={isLoading}
            className="bg-[#0a0a0a] border border-white/[0.1] text-white text-sm rounded-xl px-6 py-3 focus:outline-none focus:border-white/30 transition-colors cursor-pointer"
          >
            {availableModels.map(m => <option key={m} value={m}>{m}</option>)}
          </select>
        </div>

        {/* Zone des Messages (Scrollable) */}
        <div className="flex-1 overflow-y-auto p-12 space-y-8">
          {messages.length === 0 && !isLoading && (
             <div className="h-full flex flex-col items-center justify-center text-center opacity-30">
               <span className="text-6xl mb-4">.</span>
               <span className="text-sm tracking-widest text-glass">SYSTÈME PRÊT</span>
             </div>
          )}
          {messages.map((msg, index) => (
            <div key={index} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
              <div className={`max-w-[75%] p-6 rounded-2xl text-sm leading-relaxed ${
                msg.role === 'user' 
                  ? 'bg-white text-black shadow-[0_0_20px_rgba(255,255,255,0.1)]' 
                  : 'bg-[#111111] text-white border border-white/[0.05]'
              }`}>
                {msg.content}
              </div>
            </div>
          ))}
          {isLoading && (
             <div className="flex justify-start">
               <div className="bg-[#111111] p-6 rounded-2xl text-white border border-white/[0.05] text-sm animate-pulse">
                 Traitement...
               </div>
             </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        {/* --- ZONE DE SAISIE (Premium Input) --- */}
        <div className="p-12 pt-8">
          <div className="max-w-4xl mx-auto relative group">
            {/* Effet de bordure dynamique au focus */}
            <div className="absolute inset-0 bg-gradient-to-r from-blue-600 to-purple-600 opacity-0 group-hover:opacity-20 blur-xl transition-opacity duration-500 rounded-3xl"></div>
            
            <div className="relative bg-[#080808] border border-white/[0.06] rounded-3xl p-6 transition-all duration-300 group-hover:border-white/[0.2] group-focus-within:ring-1 ring-white/[0.1]">
               <textarea
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  placeholder="Commande système ou message..."
                  className="w-full bg-transparent text-white placeholder-neutral-600 text-lg resize-none outline-none h-24"
                  onKeyDown={(e) => { if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); handleSend(); } }}
                />
            </div>

            {/* Bouton Envoyer (Absolu) */}
            <button 
              onClick={handleSend} 
              disabled={isLoading || !input.trim()}
              className="absolute right-6 top-6 w-12 h-12 bg-white text-black rounded-xl flex items-center justify-center hover:scale-110 active:scale-95 transition-transform duration-200 shadow-[0_0_20px_rgba(255,255,255,0.3)] disabled:opacity-20 disabled:hover:scale-100"
            >
              <Send size={20} strokeWidth={2} />
            </button>
          </div>
        </div>

      </div>
    </div>
  );
};

export default AIChatPanel;