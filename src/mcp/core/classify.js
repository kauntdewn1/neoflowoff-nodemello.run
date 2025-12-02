export function classifyInput(text) {
  text = text.toLowerCase();

  if (text.includes("deploy") || text.includes("router") || text.includes("stack"))
    return "BUILD";

  if (text.includes("ideia") || text.includes("concept"))
    return "INSIGHT";

  if (text.includes("cliente") || text.includes("site") || text.includes("token"))
    return "CASE";

  if (text.includes("estratégia") || text.includes("direção"))
    return "STRATEGY";

  if (text.includes("erro") || text.includes("bug"))
    return "CRISE";

  return "GERAL";
}

