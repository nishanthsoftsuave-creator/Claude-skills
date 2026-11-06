export const tools = {
  lookup_order: async ({ id }) => ({ id, status: "shipped" }),
  // write action: no confirmation, no amount limit, no audit trail
  refund_order: async ({ id, amount }) => ({ id, refunded: amount }),
  send_email: async ({ to, body }) => ({ sent: true, to }),
};
