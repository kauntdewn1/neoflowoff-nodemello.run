export function generateThesis(event) {
  const base = {
    BUILD: "Infra muda antes da marca. E é isso que gera autoridade.",
    INSIGHT: "O futuro pertence a quem pensa em sistemas, não campanhas.",
    CASE: "Cliente pediu simples. Entregamos arquitetura.",
    STRATEGY: "A direção sempre importa mais que o conteúdo.",
    CRISE: "Toda quebra é um convite para reescrever.",
    GERAL: "O novo marketing está no backend."
  };

  return base[event] || base.GERAL;
}

