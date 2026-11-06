// Whole transcript kept forever and sent to the model on every turn.
export const history = [];
export function remember(msg) { history.push(msg); }
