import { chat } from "./model.js";
import { tools } from "./tools.js";
import { history, remember } from "./memory.js";

const SYSTEM = "You are an agent. Use tools to do what the user asks. Be helpful.";

export async function run(userRequest) {
  remember({ role: "system", content: SYSTEM });
  remember({ role: "user", content: userRequest });
  while (true) {                                   // no step limit, no stop condition
    const step = await chat(history);
    const result = await tools[step.tool](step.args);   // no validation of tool name or args
    remember({ role: "tool", content: JSON.stringify(result) });
  }
}
