// Stub model: always asks for the next tool call; never says it is done on its own.
export async function chat(messages) {
  const last = messages[messages.length - 1];
  if (last.role === "tool" && last.content.includes("error")) {
    return { tool: "lookup_order", args: { id: "A-1" } };   // retries the same call forever
  }
  return { tool: "refund_order", args: { id: "A-1", amount: 99999 } };
}
